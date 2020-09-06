import os,time
from flask import Flask,url_for,request,jsonify
from api.config import config
from api.utils import generate_response,brokerSerializer,whiteListSerializer,agencySerializer,blackListSerializer,getGeocoding,getClosestAgency
from api.csvToDB import loadCsvFilesIntoDatabase
from api.models import db,Agency,Agency_Domain_WhiteList,Broker,BlackListBrokers

app = Flask(__name__)
env_config = os.getenv('FLASK_CONFIG','dev')
app.config.from_object(config[env_config])
db.init_app(app)

"""
it creates database and schemas.
"""
with app.app_context():
    db.create_all()

"""
it loads csv files into database
"""
loadCsvFilesIntoDatabase(app)

"""
it creates database and schemas.
"""
@app.errorhandler(404)
def not_found(e):
    return generate_response(404, 'Resource not found.')


@app.errorhandler(400)
def bad_request(e):
    return generate_response(400, 'Bad request.')

"""
admin-login endpoint. it gets password and compare with the truth.
"""
@app.route("/admin-login", methods=['POST'])
def checkAdminLogin():
    passwd=request.json.get("password")
    print(passwd)
    if(passwd=="admin"):
        return generate_response(200,"Admin Logged in.")
    else:
        return generate_response(401,"Authorization Failed.")

"""
admin-broker endpoint. It retrieves form information by POST method.
Firstly, it checks broker's email domain. If the domain is in the whitelist, it fetches all possible agencies that might be assigned to the broker.
If there are multiple agencies, by calculating the distance between broker's address and agency's address, it assigns closest agency to broker.
If there is a single agency, it assigns the agency to broker.
If there is no even a single agency even though domain name is in whitelist, it generates a new agency and assigns this agency to broker.
"""
@app.route("/add-broker", methods=['POST'])
def AddBroker():
    print(request)
    firstname = request.json.get("firstname")
    lastname = request.json.get("lastname")
    email = request.json.get("email")

    brokerExists = Broker.query.filter_by(email=email).all()
    if(len(brokerExists)):
        return generate_response(400, "This e-mail address is already registered.")
    address = request.json.get("address")
    print(firstname,lastname,email,address)
    lat, lng = getGeocoding(address)
    email_domain = email.split("@")[1].replace(" ", "").replace("\n", "")
    assined_agency_id = None
    agency = Agency_Domain_WhiteList.query.filter_by(domain=email_domain).first()
    if (agency != None):  # domain in white list
        possibleAgencies = Agency.query.filter_by(domain=email_domain).all()

        if(len(possibleAgencies)==0):  # if domain is in white list but no possible agency.
            db.session.add(Agency(title=email_domain ,domain=email_domain,address=address,lat=lat,lng=lng))
            db.session.commit()
            newCreatedAgency = Agency.query.filter_by(address=address).first()
            db.session.add(
                Broker(agencyId=newCreatedAgency.id, firstname=firstname, lastname=lastname, email=email, address=address,
                       lat=lat, lng=lng))
            db.session.commit()
            return generate_response(200, "There was not any associated agency. A new one was created and connected to the broker.")
        elif (len(possibleAgencies) > 1):  # if more than one agency, then get closest one.
            agencyIndex = getClosestAgency([(agency.lat, agency.lng) for agency in possibleAgencies], (lat, lng))
            assined_agency_id = possibleAgencies[agencyIndex].id
            db.session.add(
                Broker(agencyId=assined_agency_id, firstname=firstname, lastname=lastname, email=email, address=address,
                       lat=lat, lng=lng))
            db.session.commit()

            return generate_response(200,"Broker is added succsessfully and connected to agency that located in \"" + possibleAgencies[agencyIndex].address + "\"")
        else: # choose the only available agency.
            assined_agency_id = possibleAgencies[0].id
            db.session.add(Broker(agencyId=assined_agency_id, firstname=firstname, lastname=lastname, email=email, address=address,lat=lat, lng=lng))
            db.session.commit()
            return generate_response(200,"Broker is added succsessfully and connected to single available agency that located in \"" + possibleAgencies[0].address + "\"")

    else: # broker's email domain address not in whitelist. Still, do not lose this information and save in blacklistbroker table.
        db.session.add(BlackListBrokers(domain=email_domain, firstname=firstname, lastname=lastname, email=email, address=address,lat=lat, lng=lng))
        db.session.commit()
        return generate_response(400, "Broker can not be added. Only white listed agencies can register.")

"""
get-counts endpoint. It gets statistics for home page.
"""
@app.route("/get-counts")
def getCounts():
    brokers = Broker.query.all()
    agencies = Agency.query.all()
    agenciesWhite = Agency_Domain_WhiteList.query.all()
    return jsonify({"brokers":len(brokers) , "agencies":len(agencies) ,"agenciesWhite":len(agenciesWhite) })

"""
list-brokers endpoint. It fetches brokers that exist in the database.
If it gets pagination parameters, it fetches corresponding broker data.
"""
@app.route("/list-brokers", methods=['GET'])
def listBrokers():
    page = request.args.get("page")
    perpage = request.args.get("per_page")
    ls = None
    totalCount = Broker.query.count()
    if (page != None and perpage != None):
        ls = Broker.query.offset((int(page) - 1) * int(perpage)).limit(int(perpage)).all()
    else:
        ls = Broker.query.all()

    if(len(ls)>0):
        resp=[*map(brokerSerializer, ls)]
        return jsonify({"data":resp,"total": totalCount})
    else:
        return generate_response("400", " Invalid Payload ")

"""
white-list endpoint. It fetches whitelist domains that exist in the database.
If it gets pagination parameters, it fetches corresponding whitelist domain data.
"""
@app.route("/white-list", methods=['GET'])
def listWhiteList():
    page = request.args.get("page")
    perpage = request.args.get("per_page")
    ls = None
    totalCount = Agency_Domain_WhiteList.query.count()
    if (page != None and perpage != None):
        ls = Agency_Domain_WhiteList.query.offset((int(page) - 1) * int(perpage)).limit(int(perpage)).all()
    else:
        ls = Agency_Domain_WhiteList.query.all()

    if(len(ls)>0):
        resp=[*map(whiteListSerializer, ls)]
        return jsonify({"data":resp,"total":totalCount})
    else:
        return generate_response("400", " Invalid Payload ")

"""
black-list-brokers endpoint. It fetches blacklisted brokers that had tried to registered but couldn't because their emails' domain does not match with the ones in white list.
If it gets pagination parameters, it fetches corresponding blacklisted brokers data.
"""
@app.route("/black-list-brokers", methods=['GET'])
def listBlackList():
    page = request.args.get("page")
    perpage = request.args.get("per_page")
    ls = None
    totalCount = BlackListBrokers.query.count()
    if (page != None and perpage != None):
        ls = BlackListBrokers.query.offset((int(page) - 1) * int(perpage)).limit(int(perpage)).all()
    else:
        ls = BlackListBrokers.query.all()

    if(len(ls)>0):
        resp=[*map(blackListSerializer, ls)]
        return jsonify({"data":resp,"total":totalCount})
    else:
        return generate_response("400", " Invalid Payload ")

"""
agency-list endpoint. It fetches agencies that exist in database.
If it gets pagination parameters, it fetches corresponding agency data.
"""
@app.route("/agency-list", methods=['GET'])
def listAgencies():
    page = request.args.get("page")
    perpage = request.args.get("per_page")
    ls=None
    totalCount = Agency.query.count()
    if(page != None and perpage !=None):
        ls = Agency.query.offset((int(page)-1)*int(perpage)).limit(int(perpage)).all()
    else:
        ls = Agency.query.all()

    if(len(ls)>0):
        resp=[*map(agencySerializer, ls)]
        return jsonify({"data":resp,"total":totalCount})
    else:
        return generate_response("400", " Invalid Payload ")

