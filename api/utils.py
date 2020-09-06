from flask import jsonify


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



