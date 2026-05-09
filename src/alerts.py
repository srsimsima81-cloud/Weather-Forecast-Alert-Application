def generate_alerts(data):

    alerts = []

    if not data:
        return ["API Error: Unable to fetch data"]

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    if temp > 40:
        alerts.append("Extreme heat warning")

    elif temp > 35:
        alerts.append("High temperature warning")

    if humidity > 85:
        alerts.append("High humidity detected")

    if "rain" in condition.lower():
        alerts.append("Rain expected")

    return alerts