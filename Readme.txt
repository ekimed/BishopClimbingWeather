A simple webpage that shows the 10-day forecast for Bishop, CA, a world-class bouldering destination (my favorite place to climb).


updateweather.py
Weather data is retrieved as a JSON file from the Wunderground API.

getweather.py
weekday, temperature, and condition are retrieved from the JSON file.

routes.py
employs Flask to render templates

templates
contains html templates using the jinja2 templating engine

static 
contains css files

