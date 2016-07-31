import requests
import time
import os.path
import random

url = "http://192.168.119.180:8080/"


def getNewCoords(index):
    #each line is in the format:
    # latitude,longitude
    f = open('route.txt','r')
    coordenates = list(f)
    location = coordenates[index].split(",")
    f.close()
    index = index % len(coordenates)
    return (location[0], location[1])

def simulatePeople(room):
    number=random.randint(0,2)
    if number == 0 and room > 5:
        room -= random.randint(1,6)
    elif number == 1:
        room += random.randint(1,7)
    if number > 100:
        number=100
    return number

if __name__ == '__main__':
    index = 0
    percentage = random.randint(6, 30)
    new = True
    stack = [1,2,3,4,5,6,7,8]
    eta = None
    nextStation = 8
    prevStation = 9
    while new:
	lat, lon = getNewCoords(index)
	percentage = simulatePeople(percentage)
        payload = {
            "lat": float(lat),
            "lon": float(lon),
        }
        print payload
        r = requests.get(url+"json/closest", params= payload)
        print r.json()['id']
        if os.path.isfile("id.txt"):
            indexFile = open('id.txt','r')
            identification = int(indexFile.readline())
            print "Update bus"
            payload = {
                "id" : identification,
                "lat": lat,
                "lon": lon,
                "cap": percentage,
                "prevstation": prevStation,
                "nextstation": nextStation,
            }
            print payload
            r = requests.post(url+"bus/update", data = payload)
            print r.text
        else:
            print "New bus"
            payload = {
                "lat": lat,
                "lon": lon,
                "cap": percentage,
                "prevstation": 9,
                "nextstation": 8,
            }
            print payload
            r = requests.post(url+"bus/create", data = payload)
            f = open('id.txt','w')
            data = str(r.text).split(',')
            f.write(data[0])
            f.close()
        new = False
        time.sleep(4)
        index += 1


