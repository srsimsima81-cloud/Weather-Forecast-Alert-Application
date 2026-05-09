import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

# =========================
# CURRENT WEATHER
# =========================
def fetch_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    res = requests.get(url)

    if res.status_code != 200:
        return None

    data = res.json()

    if data.get("cod") != 200:
        return None

    return data


# =========================
# FORECAST WEATHER 
# =========================
def fetch_forecast(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    res = requests.get(url)

    if res.status_code != 200:
        return None

    data = res.json()

    if data.get("cod") != "200":
        return None

    return data