# 🍃 WeatherSphere 🌀

## 🌦️ Live Weather Intelligence & Forecast System

WeatherSphere is a futuristic weather dashboard built using **Python, Streamlit, and OpenWeather API**. It provides real-time weather updates, multi-day forecasts, intelligent alerts, analytics, and interactive satellite mapping with a modern Apple-style UI experience.

---

## 🚀 Features

- 🌡️ Real-time weather data (temperature, humidity, wind, condition)
- 📅 5-day weather forecast engine
- ⚠️ Smart weather alerts system
- 📊 Analytics with charts and trend visualization
- 🛰️ Interactive satellite-style weather map (Folium)
- 📄 Automatic report generation (CSV export)
- 🎨 Dynamic UI with temperature-based background gradients
- 💎 Glassmorphism UI with neon-style text glow
- 🍏 Apple Weather-inspired design system
- ⚡ Fast Streamlit web interface

---

## 🏗️ Project Structure

---

Weather-Forecast-Alert-Application/
│
├── dashboard.py                  # Main Streamlit application (UI + logic)
├── requirements.txt              # Project dependencies
├── README.md                     # Project documentation
│
├── src/                          # Core backend modules
│   ├── __init__.py              # Makes src a Python package
│   ├── weather_api.py           # API calls (current + forecast)
│   ├── forecast.py              # Forecast parsing & processing
│   ├── alerts.py                # Weather alert engine
│   ├── visualization.py        # Charts & analytics generator
│   └── report_generator.py     # Report/CSV export system
│
├── notebooks/                   # Jupyter experimentation
│   └── WeatherSphere.ipynb     # Data analysis & testing
│
├── outputs/                     # Generated outputs
│   ├── reports/                 # CSV weather reports
│   └── charts/                  # Visualization images
│
├── venv/                        # Virtual environment (ignored in GitHub)
│
└── .env                         # API keys (OpenWeather API key)

---

## 🧠 Tech Stack

- Python 🐍
- Streamlit ⚡
- OpenWeather API 🌍
- Pandas 📊
- Matplotlib 📈
- Folium 🛰️
- Jupyter Notebook 📓

---

## ⚙️ Installation & Setup

```bash
# Clone repository
git clone https://github.com/srsimsima81-cloud/Weather-Forecast-Alert-Application.git

# Navigate to project
cd Weather-Forecast-Alert-Application

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run dashboard.py