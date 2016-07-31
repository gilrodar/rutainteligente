import requests
import time
import os.path
import random

url = "http://192.168.119.180:8080/bus/"

if __name__ == '__main__':
    payload = {
            "lat": 19.472092,
            "lon": -99.13600,
            }
    print payload
    r = requests.get(url+"closest", params= payload)
    print str(r.text)
    payload = {
	"lat": lat,
	"lon": lon,
	"cap": percentage,
	"prevstation": 9,
	"nextstation": 8,
    }
    print payload
    r = requests.post(url+"bus/create", data = payload)

