import os
from weatherApi import handler 

# set API key for testing (replace with your actual key or use environment variable)
os.environ["WEATHER_API_KEY"] = "e6464df42cc44592436cc885d7197a3a"

# create dummy request object
class DummyRequest:
    def __init__(self):
        self.args = {"city": "Delhi"}


response = handler(DummyRequest())

if response["statusCode"] == 200:
    data = response["body"]

    print(f"{'Datetime':20} {'Temp':6} {'Humidity':8} {'Condition':10} {'Wind':6}")
    print("-" * 60)

    for item in data:
        print(f"{item['datetime']:20} {item['temperature']:6} {item['humidity']:8} {item['condition']:10} {item['wind_speed']:6}")