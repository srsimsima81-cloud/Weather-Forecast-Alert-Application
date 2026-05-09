from src.weather_api import fetch_weather
from src.alerts import generate_alerts
from src.report_generator import save_report
from src.visualization import generate_chart
from src.utils import create_folders

create_folders()

city = input("Enter city name: ")

data = fetch_weather(city)

if not data:
    print("Error fetching weather data")
    exit()

alerts = generate_alerts(data)

report_file = save_report(data, alerts)

generate_chart(data)

print("\nWeather Report")
print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")
print("Humidity:", data["main"]["humidity"], "%")
print("Condition:", data["weather"][0]["description"])
print("Wind Speed:", data["wind"]["speed"], "m/s")

print("\nAlerts:")
for a in alerts:
    print("-", a)

print("\nReport saved at:", report_file)