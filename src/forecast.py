import pandas as pd

def parse_forecast(data):

    forecast_list = []

    for item in data["list"]:

        forecast_list.append({
            "datetime": item["dt_txt"],
            "temp": item["main"]["temp"],
            "humidity": item["main"]["humidity"],
            "condition": item["weather"][0]["description"]
        })

    return pd.DataFrame(forecast_list)