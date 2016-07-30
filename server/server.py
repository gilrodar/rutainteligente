
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
# from database_setup import

import json
import httplib2
from flask import make_response
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return "pagina principal para web con interaccion"


@app.route('/estacionaria')
def index():
    return "pagina principal para web sin interaccion"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)

