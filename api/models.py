from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

"""
Agency Domain WhiteList Table Structure
"""
class Agency_Domain_WhiteList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

"""
Agency Table Structure
"""
class Agency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    domain = db.Column(db.String(255), db.ForeignKey(Agency_Domain_WhiteList.domain))
    address = db.Column(db.String(255), nullable=False, unique=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

"""
Broker Table Structure
"""
class Broker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agencyId = db.Column(db.Integer, db.ForeignKey(Agency.id))
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

"""
BlackListed Broker Table Structure
"""
class BlackListBrokers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

