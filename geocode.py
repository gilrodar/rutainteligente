import httplib2
import json

def getGeocodeLocation(inputString):
    locationString = inputString.replace(" ","+")
    google_api_key = "AIzaSyAy6ysiX_N0M2TKdTPbImN0P6Ccgbh1dm8"
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (locationString, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)

address = raw_input()
print (getGeocodeLocation(address))

