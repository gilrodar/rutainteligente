import requests
import time
import os.path
import random

url = "http://192.168.119.180:8080/json/"

if __name__ == '__main__':
    payload = {
            "lat": 19.472092,
            "lon": -99.13600,
            }
    print payload
    r = requests.post(url+"closest", data = payload)
    print str(r.text)

