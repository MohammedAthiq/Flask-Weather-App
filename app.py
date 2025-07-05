from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = {
                "city": city.title(),
                "temperature": data['main']['temp'],
                "description": data['weather'][0]['description'].title()
            }
        else:
            error = "City not found. Please check the spelling."
    
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)