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
    while index < 3:
        lat, lon = getNewCoords(index)
        percentage = random.randint(6,100)
        prevStation = random.randint(2,9)
        number=random.randint(0,2)
        if number:
            nextStation = prevStation + 1
        else:
            nextStation = prevStation - 1
        print index
        percentage = simulatePeople(percentage)
        print "New bus"
        payload = {
                "lat": float(lat),
                "lon": float(lon),
                "cap": percentage,
                "prevstation": prevStation,
                "nextstation": nextStation,
                }
        print payload
        r = requests.post(url+"bus/create", data = payload)
        index += 1


