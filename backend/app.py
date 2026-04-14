from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from weatherApi import handler

app = Flask(__name__)

# 🔥 FORCE CORS (important)
CORS(app, supports_credentials=True)

# API key
os.environ["WEATHER_API_KEY"] = "e6464df42cc44592436cc885d7197a3a"

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response

@app.route("/")
def home():
    return "Weather API is running 🚀"

@app.route("/api/weather", methods=["GET"])
def weather():
    response = handler(request)
    return jsonify(response["body"])

if __name__ == "__main__":
    app.run(debug=True)