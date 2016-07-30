
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Station, Bus

import json
import httplib2
from flask import make_response
import requests


app = Flask(__name__)

#Connect to Database and create database session
engine = create_engine('sqlite:///stationsandbuses.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
    return "pagina principal para web con interaccion"


@app.route('/estacionaria')
def indexForStation():
    return "pagina principal para web sin interaccion"


# Endpoint for buses data
@app.route('/json/buses')
def busesJSON():
    buses = session.query(Bus).all()
    return jsonify(buses = [b.serialize for b in buses])

# Endpoint for stations data
@app.route('/json/stations')
def stationsJSON():
    stations = session.query(Station).all()
    return jsonify(stations = [s.serialize for s in stations])

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)

