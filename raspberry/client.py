import requests
import time
import os.path
import random

url = "http://192.168.119.180:8080/bus/"

if __name__ == '__main__':
    index = 0
	percentage = randint(6, 30)
    new = True
    while new:
	lat, lon = getNewCoords(index)
	percentage = simulatePeople(percentage)
        if os.path.isfile("id.txt"):
            indexFile = open('id.txt','r')
            identification = int(indexFile.readline())
            print "Update bus"
            payload = {
                "id" : identification
                "lat": lat,
                "lon": lon,
                "cap": percentage,
                "prevstation": 1,
                "nextstation": 2,
            }
            print payload
            r = requests.post(url+"create", data = payload)
            print str(r.text)
        else:
            print "New bus"
            payload = {
                "lat": lat,
                "lon": lon,
                "cap": percentage,
                "prevstation": 1,
                "nextstation": 2,
            }
            print payload
            r = requests.post(url+"create", data = payload)
            f = open('id.txt','w')
            f.write(str(r.text))
            f.close()
            new = False
        time.sleep(15)
        index += 1


def getNewCoords(index):
    #each line is in the format:
    # latitude,longitude
    f = open('coordenates.txt','r')
    coordenates = list(f)
    location = coordenates[index].split(",")
    f.close()
    index = index % len(coordenates)
    return (location[0], location[1])

def simulatePeople(room)
    number=0
    number=random.randint(0,2)
    if number == 0:
        number -= random.randint(1,6)
    elif number == 1:
        number += random.randint(1,7)
    if number > 100:
        number=100
    return number

