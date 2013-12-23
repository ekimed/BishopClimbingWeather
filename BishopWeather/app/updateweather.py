#!/usr/bin/env python

import urllib2
import json
from collections import defaultdict



def parse_data(key, weatherdata):
    weather_data = defaultdict(list)
    
    required_data = weatherdata["forecast"]["simpleforecast"]["forecastday"]
    
    for item in required_data:
        weekday = item["date"]["weekday"]
        temp1 = item["high"]["fahrenheit"]
        temp2 = item["high"]["celsius"]
        cond = item["conditions"]

        #creates a list of data for each day
        hold = []
        hold.append(weekday)
        hold.append(temp1)
        hold.append(temp2)
        hold.append(cond)
        
        #append lists of values to city key
        weather_data[key].append(hold)
    return weather_data

def get_weather():
    coordinate_dict = {'Bishop':'37.3291,-118.5771'}
    for key, value in coordinate_dict.iteritems():
        #insert personal API key for Wunderground Weather
        f = urllib2.urlopen('http://api.wunderground.com/api/'+insertAPIkey+'/forecast10day/geolookup/q/'+value+'.json')
        json_string = f.read()
        weatherdata = json.loads(json_string)
        parsed_data = parse_data(key,weatherdata)
        filename='requiredData.json'
        with open(filename,"wb") as outfile:
            json.dump(parsed_data,outfile,indent=2)
        

    
def main():
    get_weather()

if __name__=='__main__':
    main()
        