import csv,os
from api.models import db,Agency,Agency_Domain_WhiteList,Broker
import googlemaps
import random
from math import sin, cos, sqrt, atan2, radians

def getGeocoding(address):
    #from random import uniform
    #x, y = uniform(-180, 180), uniform(-90, 90)
    #return x, y
    gmaps = googlemaps.Client(key='AIzaSyCEctx0RhWzg4dC46MJuSjmaJR7IYFVQP0')
    geocode_result = gmaps.geocode(address)
    return float(geocode_result[0]["geometry"]["location"]["lat"]),float(geocode_result[0]["geometry"]["location"]["lng"])


def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    print(instance)
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.items())
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        session.commit()
        print(instance)
        return instance, True

# it calculates the distance between two lat long
def getDistance(el1,el2):

    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(el1[0])
    lon1 = radians(el1[1])
    lat2 = radians(el2[0])
    lon2 = radians(el2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

# it returns closest agency index
def getClosestAgency(list,coordinates):
    distances = [getDistance(el,coordinates) for el in list]
    return distances.index(min(distances))


def loadCsvFilesIntoDatabase(app):
    fname="../files/agency_domain_whitelist.csv"
    with open(fname) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print "Column names are {" + ','.join(row) +"}"
                # print(row)
                line_count += 1
                # break
            else:
                try:
                    with app.app_context():
                        get_or_create(db.session, Agency_Domain_WhiteList, id=int(row[0]),domain=row[1])
                        #db.session.add(Agency_Domain_WhiteList(id=int(row[0]),domain=row[1]))
                        #db.session.commit()
                except Exception as e:
                    print("Exception : ", e, row)

    fname = "../files/agency.csv"
    with open(fname) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print "Column names are {" + ','.join(row) +"}"
                # print(row)
                line_count += 1
                # break
            else:
                try:
                    lat,lng=getGeocoding(row[3])
                    #break
                    with app.app_context():
                        get_or_create(db.session, Agency, id=int(row[0]), title=row[1], domain=row[2], address=row[3], lat=lat, lng=lng)
                        #db.session.add(Agency(id=int(row[0]), title=row[1], domain=row[2], address=row[3], lat=lat, lng=lng))
                        #db.session.commit()
                except Exception as e:
                    print("Exception : ", e, row)
    """
    fname = "../files/broker.csv"
    with open(fname) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print "Column names are {" + ','.join(row) +"}"
                # print(row)
                line_count += 1
                # break
            else:
                try:
                    firstname = row[0]
                    lastname = row[1]
                    email = row[2]
                    address = row[3]

                    ## convert information into more useful form.
                    lat, lng = getGeocoding(address)
                    email_domain=email.split("@")[1].replace(" ","").replace("\n","")

                    assined_agency_id=None
                    print(row)
                    with app.app_context():

                        agency = Agency_Domain_WhiteList.query.filter_by(domain=email_domain).first()
                        print(agency)
                        if(agency!=None): # domain in white list
                            possibleAgencies=Agency.query.filter_by(domain=email_domain).all()
                            print(possibleAgencies)
                            if(len(possibleAgencies)>1): # if more than one agency, then get closest one.
                                agencyIndex=getClosestAgency([(agency.lat,agency.lng) for agency in possibleAgencies],(lat,lng))
                                assined_agency_id= possibleAgencies[agencyIndex].id
                            else:
                                assined_agency_id = possibleAgencies[0].id

                            db.session.add(Broker(agencyId=assined_agency_id,firstname=firstname,lastname=lastname,email=email,address=address,lat=lat,lng=lng))
                            db.session.commit()
                except Exception as e:
                    print("Broker Exception : ", e, row)"""
