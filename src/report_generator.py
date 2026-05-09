import os
import pandas as pd

def save_report(weather_data, alerts):

    os.makedirs("outputs", exist_ok=True)

    text_output = f"""
Weather Report
--------------
City: {weather_data['name']}
Temperature: {weather_data['main']['temp']} °C
Humidity: {weather_data['main']['humidity']} %
Wind Speed: {weather_data['wind']['speed']} m/s
Condition: {weather_data['weather'][0]['description']}
Alerts: {', '.join(alerts) if alerts else 'None'}
"""

    file_path = "outputs/output.txt"

    with open(file_path, "w") as f:
        f.write(text_output)

    return file_path