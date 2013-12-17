import urllib2
import json


coordinate_dict = {'Bishop':'37.3291,-118.5771'}
for key, value in coordinate_dict.iteritems():
    #insert personal API key from Wunderground API
    f = urllib2.urlopen('http://api.wunderground.com/api/apikey/forecast10day/geolookup/q/'+value+'.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    filename = key+'.json'
    with open(filename, "wb") as outfile:
        json.dump(parsed_json, outfile, indent=6)


