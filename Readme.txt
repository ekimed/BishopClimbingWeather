A simple webpage that shows the 10-day forecast for Bishop, CA, a world-class bouldering destination (my favorite place to climb).


updateweather.py
Weather data is retrieved as a JSON file from the Wunderground API. This file gets updated every 4 hours (re: crontest.txt). Data gets parsed and necessary data gets extracted and written to new JSON file named ‘requiredData.json’


routes.py
employs Flask to render templates

crontest.txt
A text file containing a cronjob that runs the updateweather.py python script every 4 hours. Add this to crontab.

templates
Contains html templates using the jinja2 templating engine.

static 
Contains css file.

