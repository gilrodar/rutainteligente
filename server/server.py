
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Station, Bus
import json
import httplib2
from flask import make_response
import requests

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

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
@crossdomain(origin='*')
def busesJSON():
    buses = session.query(Bus).all()
    return jsonify(buses = [b.serialize for b in buses])

# Endpoint for stations data
@app.route('/json/stations')
@crossdomain(origin='*')
def stationsJSON():
    stations = session.query(Station).all()
    return jsonify(stations = [s.serialize for s in stations])

# Create new busand assign the id
@app.route('/bus/create', methods = ['POST'])
def newBus():
    if request.method == 'POST':
        nextStation = session.query(Station).filter_by(id = request.form['nextstation']).one()
        eta = getETABetween([float(request.form['lat']), float(request.form['lon'])],
                [nextStation.latitude, nextStation.longitude])
        bus = Bus (
	    longitude = request.form['lon'],
	    latitude = request.form['lat'],
	    next_station = request.form['prevstation'],
	    prev_station = request.form['nextstation'],
	    time_to_next_station = eta,
	    room = request.form['cap']
	)
        session.add(bus)
        session.flush()
        index = bus.id
        session.commit()
        return str(index)
    else:
        return "not post reques"

# Update coords of the bus
@app.route('/bus/update', methods = ['POST'])
def editBus():
    if request.method == 'POST':
        nextStation = session.query(Station).filter_by(id = request.form['nextstation']).one()
        bus = session.query(Bus).filter_by(id = request.form['id']).one()
        eta = getETABetween([request.form['lat'], request.form['lon']],
                [nextStation.latitude, nextStation.longitude])
        bus.longitude = request.form['lon'],
        bus.latitude = request.form['lat'],
        bus.next_station = request.form['prevstation'],
        bus.prev_station = request.form['nextstation'],
        bus.time_to_next_station = eta,
        bus.room = request.form['cap']
        session.add(bus)
        session.commit()
        return eta
    else:
        return "not post reques"


def getETABetween(locationOne, locationTwo):
    google_key_secret ="AIzaSyDafqyfJNYmaMFDciA8WESdmulQ5dObn_U"
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s,%s&destinations=%s,%s&mode=driving&language=es-ES&key=%s" % (locationOne[0], locationOne[1],locationTwo[0], locationTwo[1], google_key_secret)
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    eta = result["rows"][0]["elements"][0]["duration"]["value"]
    return eta

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)

