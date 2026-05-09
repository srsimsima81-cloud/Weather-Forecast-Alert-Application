# 🍃 WeatherSphere 🌀  
### Live Weather Intelligence + Forecast + Visualization System

---

## 🌟 Overview
WeatherSphere is a modern weather intelligence web application built using Python and Streamlit.

It provides real-time weather updates, forecasts, alerts, analytics, and a dynamic UI that adapts based on weather conditions.

---

## 🚀 Features

### 🌡️ Real-Time Weather
- Temperature, humidity, wind speed
- Live weather condition detection

### 📈 Forecast System
- Multi-day forecast support
- Trend-based visualization

### ⚠️ Smart Alerts
- Heat warnings
- Rain alerts
- Wind alerts

### 🗺️ Interactive Map
- City-based location mapping
- Dark/satellite style visualization

### 🎨 Dynamic UI
- Temperature-based gradient backgrounds
- Glassmorphism cards
- Neon-style soft glow text
- Animated title intro

---

## 🏗️ Project Structure

Weather-Forecast-Alert-Application/
│
├── dashboard.py                     # Main Streamlit application (UI + logic)
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation
│
├── src/                            # Core backend modules
│   ├── __init__.py                 # Makes src a Python package
│   ├── weather_api.py             # Current weather + forecast API calls
│   ├── forecast.py                # Forecast parsing & transformation
│   ├── alerts.py                  # Weather alert logic engine
│   ├── visualization.py           # Charts & analytics generation
│   └── report_generator.py        # CSV/report export system
│
├── notebooks/                     # Jupyter analysis & experimentation
│   └── WeatherSphere.ipynb        # Data exploration + testing
│
├── outputs/                       # Generated reports & exports
│   ├── reports/                   # CSV weather reports
│   └── charts/                    # Generated graphs/images
│
│
├── venv/                          # Virtual environment (NOT push to GitHub)
│
└── .env                           # API keys (OpenWeather API key) 

---

## 🌍 Test Cities

- Jaisalmer (🔥 Extreme Heat)  
- Hyderabad (🌤 Hot & Humid)  
- London (🌧 Rainy)  
- Toronto (❄ Cold)  
- Kochi (🌦 Monsoon)  

---

## ⚙️ Setup

1. Install dependencies  
   pip install -r requirements.txt  

2. Add API key in `.env`  
   API_KEY=your_key  

3. Run app  
   streamlit run dashboard.py  

---

## 🎯 Highlights
✔ Dynamic weather UI  
✔ Forecast analytics  
✔ Map integration  
✔ Glassmorphism design  
✔ Animated title system  

---

