from flask import Flask, render_template
import json


app = Flask(__name__)

@app.route('/')
def home():
    with open('requiredData.json') as f:
        data = f.read()
        jsondata = json.loads(data)
        for value in jsondata.itervalues():
            return render_template('home.html', weather_data=value)

if __name__=='__main__':
    app.run(debug=True)