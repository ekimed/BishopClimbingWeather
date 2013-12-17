from flask import Flask, render_template
import getweather


weather_data = getweather.getweather('Bishop.json')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', weather_data=weather_data)

if __name__=='__main__':
    app.run(debug=True)