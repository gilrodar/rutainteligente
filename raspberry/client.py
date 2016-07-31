import requests
import time
import os.path

url = "http://192.168.119.90:8080/bus/"


def getNewCoords(index):
    #each line is in the format:
    # latitude,longitude
    f = open('coordenates.txt','r')
    coordenates = list(f)
    location = coordenates[index].split(",")
    f.close()
    index = index % len(coordenates)
    return (location[0], location[1])



if __name__ == '__main__':
    index = 0
    new = True
    while new:
        lat, lon = getNewCoords(index)
        if os.path.isfile("id.txt"):
            new = False
            pass
        else:
            print "New bus"
            payload = {
                "lat": lat,
                "lon": lon,
                "cap": 100,
                "prevstation": 1,
                "nextstation": 2,
            }
            print payload
            r = requests.post(url+"create", data = payload)
            f = open('id.txt','w')
            f.write(str(r.text))
            f.close()
        time.sleep(15)
        index += 1

