
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
    return render_template('index.html')

@app.route('/estacionaria')
def indexForStation():
    return "pagina principal para web sin interaccion"


# Endpoint for buses data
@app.route('/json/buses')
@crossdomain(origin='*')
def busesJSON():
    buses = session.query(Bus).all()
    return jsonify(buses = [b.serialize for b in buses])

# Endpoint for cercano
@app.route('/json/closest')
@crossdomain(origin='*')
def closestJSON():
    stations = session.query(Station).all()
    identification = 1
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins='
    for s in stations:
	url += '%s,%s' % (s.latitude, s.longitude)
	if s.id != 9:
	    url += '|'
    url += '&destinations='
    url += '%s,%s' % (request.args.get('lat'), request.args.get('lon') )
    url += '&mode=walking&language=es-ES&key=AIzaSyDafqyfJNYmaMFDciA8WESdmulQ5dObn_U'

    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    rows = result['rows']
    minimal = None
    indexOfMinimal = 0
    index = 1
    for r in rows:
        current = r['elements'][0]['distance']['value']
        if minimal is not None:
            if current < minimal:
                minimal = current
                indexOfMinimal = index
        else:
            minimal = current
            indexOfMinimal = index
        index += 1
    return jsonify(id = indexOfMinimal)



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
        eta = getETABetween(float(request.form['lat']), float(request.form['lon']),
                            nextStation.latitude, nextStation.longitude)
        bus = Bus (
            longitude = float(request.form['lon']),
            latitude = float(request.form['lat']),
            next_station = request.form['nextstation'],
            prev_station = request.form['prevstation'],
            time_to_next_station = eta,
            room = request.form['cap']
        )
        session.add(bus)
        session.flush()
        index = bus.id
        session.commit()
        return str(index) +","+str(eta)
    else:
        return "not post reques"

# Update coords of the bus
@app.route('/bus/<int:bus_id>/update/', methods = ['POST'])
def editBus(bus_id):
    if request.method == 'POST':
        bus = session.query(Bus).filter_by(id = bus_id).one()
        nextStation = session.query(Station).filter_by(id = bus.next_station).one()
        eta = getETABetween(float(request.form['lat']), float(request.form['lon']),
                            nextStation.latitude, nextStation.longitude)
        if request.form['lon']:
            bus.longitude = float(request.form['lon']),
        if request.form['lat']:
            bus.latitude = float(request.form['lat']),
        if request.form['nextstation']:
            bus.next_station = request.form['nextstation'],
        if request.form['prevstation']:
            bus.prev_station = request.form['prevstation'],
        if request.form['cap']:
            bus.room = request.form['cap']
        bus.time_to_next_station = eta,
        session.add(bus)
        session.commit()
        return str(eta)
    else:
        return "not post reques"


def getETABetween(latOne, lonOne, latTwo, lonTwo):
    google_key_secret ="AIzaSyDafqyfJNYmaMFDciA8WESdmulQ5dObn_U"
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s,%s&destinations=%s,%s&mode=driving&language=es-ES&key=%s" % (latOne, lonOne,latTwo, lonTwo, google_key_secret)
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    eta = result["rows"][0]["elements"][0]["duration"]["value"]
    return eta



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)

