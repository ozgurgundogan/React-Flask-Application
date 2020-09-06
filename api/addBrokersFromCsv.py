import requests,csv,json
from utils import getGeocoding
from flask import Flask,url_for,request,jsonify

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
               email = "b" + row[2]
               address = row[3]
               password = "dasdsafsd32123"
               ## convert information into more useful form.
               lat, lng = getGeocoding(address)
               email_domain=email.split("@")[1].replace(" ","").replace("\n","")

               assined_agency_id=None
               print(row)

               url = 'http://localhost:5000/add-broker'
               myobj = {'firstname': firstname, 'lastname':lastname, 'email':email , 'address':address}

               x = requests.post(url, json=myobj)
               print(x)

           except Exception as e:
               print("Broker Exception : ", e, row)

