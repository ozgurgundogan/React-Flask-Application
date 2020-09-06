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
                    print("Broker Exception : ", e, row)