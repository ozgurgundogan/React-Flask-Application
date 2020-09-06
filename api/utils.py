from flask import jsonify
import googlemaps
import random
from math import sin, cos, sqrt, atan2, radians

"""
Generic response generation function.
"""
def generate_response(code, message):
    if(code==200):
        return jsonify({'code': code,  'error': False,'message': message})
    elif(code==300):
        return jsonify({'code': code,  'error': True, 'message': message})
    else:
        return jsonify({'code': code,  'error': True, 'message': message})


"""
This function is used to convert db-row values to dict.
"""
def brokerSerializer(row):
    return {"id": row.id,
            "agencyId": row.agencyId,
            "firstname": row.firstname,
            "lastname": row.lastname,
            "email": row.email,
            "address": row.address,
            "timestamp": row.timestamp.strftime("%m/%d/%Y, %H:%M:%S")}

"""
This function is used to convert db-row values to dict.
"""
def blackListSerializer(row):
    return {"id": row.id,
            "domain": row.domain,
            "firstname": row.firstname,
            "lastname": row.lastname,
            "email": row.email,
            "address": row.address,
            "timestamp": row.timestamp.strftime("%m/%d/%Y, %H:%M:%S")}

"""
This function is used to convert db-row values to dict.
"""
def whiteListSerializer(row):
    return {"id": row.id,
     "domain": row.domain,
     "timestamp": row.timestamp.strftime("%m/%d/%Y, %H:%M:%S")}

"""
This function is used to convert db-row values to dict.
"""
def agencySerializer(row):
    return {"id": row.id,
            "title": row.title,
            "domain": row.domain,
            "address": row.address,
            "lat": row.lat,
            "lng": row.lng,
            "timestamp": row.timestamp}



def getGeocoding(address):
    gmaps = googlemaps.Client(key='AIzaSyCEctx0RhWzg4dC46MJuSjmaJR7IYFVQP0')
    geocode_result = gmaps.geocode(address)
    return float(geocode_result[0]["geometry"]["location"]["lat"]),float(geocode_result[0]["geometry"]["location"]["lng"])

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
