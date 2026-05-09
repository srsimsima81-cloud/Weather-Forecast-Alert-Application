import matplotlib.pyplot as plt
import os

def generate_chart(data):

    os.makedirs("images", exist_ok=True)

    labels = ["Temp", "Humidity", "Wind Speed"]

    values = [
        data["main"]["temp"],
        data["main"]["humidity"],
        data["wind"]["speed"]
    ]

    plt.figure(figsize=(6,4))
    plt.bar(labels, values)

    plt.title("Weather Analytics")

    file_path = f"images/{data['name']}_chart.png"
    plt.savefig(file_path)

    plt.close()

    return file_path