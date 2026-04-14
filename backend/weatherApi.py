import os
import requests


def handler(request):
    """
    Serverless function to fetch weather forecast data
    """

    api_key = os.environ.get("WEATHER_API_KEY")

    city = request.args.get("city")
    

    if not api_key:
        return {
            "statusCode": 500,
            "body": {"error": "API key not configured"}
        }

    url = (
        "http://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if "list" not in data:
            return {
                "statusCode": 400,
                "body": {"error": "Invalid city or API response"}
            }

        formatted = []
        for item in data["list"]:
            formatted.append({
                "datetime": item["dt_txt"],
                "temperature": item["main"]["temp"],
                "humidity": item["main"]["humidity"],
                "condition": item["weather"][0]["main"],
                "wind_speed": item["wind"]["speed"]
            })

        return {
            "statusCode": 200,
            "body": formatted
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": {"error": str(e)}
        }