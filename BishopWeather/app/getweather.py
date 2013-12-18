import urllib2
import json
from collections import defaultdict



weather_data = defaultdict(list)

def getweather(filename):    
    location = open(filename)
    data = json.load(location)
    
    #list of dicts
    weatherdata = data["forecast"]["simpleforecast"]["forecastday"]
    
    counter = 0
    for item in weatherdata:
        weekday = item["date"]["weekday"]
        temp1 = item["high"]["fahrenheit"]
        temp2 = item["high"]["celsius"]
        cond = item["conditions"]
        
        counter = counter + 1
        
        weather_data[counter].append(weekday)
        weather_data[counter].append(temp1)
        weather_data[counter].append(temp2)
        weather_data[counter].append(cond)
        
    return weather_data





        
    

