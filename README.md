# 🍃 WeatherSphere 🌀  
### 🌦️ Live Weather Intelligence & Forecast System

---

## 📌 Overview  
WeatherSphere is a futuristic weather intelligence dashboard built using Python, Streamlit, and OpenWeather API. It provides real-time weather updates, multi-day forecasts, intelligent alerts, analytics, and interactive satellite mapping with an Apple-style UI featuring neon glow effects and dynamic temperature-based themes.

---

## 🚀 Features  
🌡️ Real-time weather data (temperature, humidity, wind, condition)  
📅 5-day weather forecast engine  
⚠️ Smart weather alert system  
📊 Weather analytics with charts and trends  
🛰️ Interactive satellite-style map (Folium integration)  
📄 Automatic report generation (CSV export)  
🎨 Dynamic UI with temperature-based gradient backgrounds  
💎 Glassmorphism UI with neon glow effects  
🍏 Apple Weather-inspired design system  
⚡ Fast and responsive Streamlit web interface  

---

## 🏗️ Project Structure  
```text
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
└── .env                         # API key (OpenWeather API)
```

---

## 🧠 Tech Stack  
Python 🐍 | Streamlit ⚡ | OpenWeather API 🌍 | Pandas 📊 | Matplotlib 📈 | Folium 🛰️ | Jupyter 📓  

---

## ⚙️ Installation & Setup  
```bash
git clone https://github.com/srsimsima81-cloud/Weather-Forecast-Alert-Application.git
cd Weather-Forecast-Alert-Application
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
streamlit run dashboard.py
```

---

## 🔑 Environment Variables  
```text
API_KEY=your_openweather_api_key
```

---

## 📊 System Workflow  
User Input → API Call → Weather Data → Forecast Engine → Alerts → Analytics → Dashboard → Report Generation  

---

## 📌 Future Enhancements  
🌐 Global radar maps  
🤖 AI weather prediction  
📱 Mobile optimization  
📡 Live animated weather radar  
☁️ Cloud deployment (Streamlit Cloud)  

---

