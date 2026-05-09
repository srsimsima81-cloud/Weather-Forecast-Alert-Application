import streamlit as st
import folium
from streamlit_folium import st_folium

from src.weather_api import fetch_weather, fetch_forecast
from src.alerts import generate_alerts
from src.report_generator import save_report
from src.forecast import parse_forecast

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="WeatherSphere", layout="wide")
# =========================
# UI STYLE 
# =========================
st.markdown("""
<style>

/* =========================
   APP BACKGROUND
========================= */
.stApp {
    background: #05070f !important;
}

/* REMOVE STREAMLIT BACKGROUNDS */
.block-container, .main, section {
    background: transparent !important;
}

/* =========================
   TEXT STYLE 
========================= */
p, span, label, div {
    color: white !important;
    text-shadow: 0 0 6px rgba(255,255,255,0.15);
}

/* =========================
   HEADINGS 
========================= */
h2, h3 {
    text-shadow:
        0 0 8px rgba(125,211,252,0.5),
        0 0 18px rgba(56,189,248,0.3);
}

/* =========================
   GLASS CARDS
========================= */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.06) !important;
    border-radius: 14px;
    padding: 12px;
    backdrop-filter: blur(14px);
}

/* =========================
   INPUT STYLE
========================= */
input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: white !important;
}

/* =========================
   FIX MAP BACKGROUND
========================= */
div[data-testid="stIframe"],
iframe {
    background: transparent !important;
    border-radius: 16px !important;
}

/* =========================
    TITLE 
========================= */
.ws-title {
    text-align: center;
    font-size: 52px;
    font-weight: 700;
    color: white;

    opacity: 0;
    filter: blur(14px);
    transform: scale(1.2);

    animation: titleReveal 2.2s ease-out forwards;

    
    text-shadow:
        0 0 4px rgba(255,255,255,0.55),
        0 0 10px rgba(255,255,255,0.35),
        0 0 20px rgba(255,255,255,0.25);
}

/* =========================
   TITLE ANIMATION
========================= */
@keyframes titleReveal {

    0% {
        opacity: 0;
        filter: blur(14px);
        transform: scale(1.2);
        text-shadow: none;
    }

    60% {
        opacity: 0.6;
        filter: blur(6px);
    }

    100% {
        opacity: 1;
        filter: blur(0);
        transform: scale(1);

        
        text-shadow:
            0 0 4px rgba(255,255,255,0.55),
            0 0 10px rgba(255,255,255,0.35),
            0 0 20px rgba(255,255,255,0.25);
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE 
# =========================
st.markdown("""
<div class="ws-title">🍃 WeatherSphere 🌀</div>
""", unsafe_allow_html=True)

st.write("Live Weather Intelligence + Forecast System")


# =========================
# BACKGROUND ENGINE
# =========================
def apply_background(temp):

    if temp <= 0:
        bg = "linear-gradient(to right, #0F2027, #203A43, #2C5364)"
    elif temp <= 10:
        bg = "linear-gradient(to right, #83a4d4, #b6fbff)"
    elif temp <= 20:
        bg = "linear-gradient(to right, #A1C4FD, #C2E9FB)"
    elif temp <= 28:
        bg = "linear-gradient(to right, #43e97b, #38f9d7)"
    elif temp <= 34:
        bg = "linear-gradient(to right, #f7971e, #ffd200)"
    elif temp <= 40:
        bg = "linear-gradient(to right, #ff512f, #f09819)"
    else:
        bg = "linear-gradient(to right, #8B0000, #FF4500, #FFD700)"

    st.markdown(f"""
    <style>
    .stApp {{
        background: {bg} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# =========================
# MAP
# =========================

def show_map(lat, lon, city, temp, condition):

    import folium
    from streamlit_folium import st_folium

    # =========================
    # BASE MAP 
    # =========================
    m = folium.Map(
        location=[lat, lon],
        zoom_start=11,
        tiles="Esri World Imagery",
        control_scale=True
    )

    # =========================
    # LOCATION MARKER 
    # =========================
    folium.Marker(
        [lat, lon],
        tooltip=city,
        icon=folium.DivIcon(html=f"""
        <div style="
            width: 14px;
            height: 14px;
            background: #00f0ff;
            border-radius: 50%;
            box-shadow: 0 0 10px #00f0ff, 0 0 25px #00f0ff;
            animation: pulse 1.5s infinite;
        "></div>

        <style>
        @keyframes pulse {{
            0% {{
                transform: scale(0.8);
                opacity: 0.8;
            }}
            50% {{
                transform: scale(2);
                opacity: 0.3;
            }}
            100% {{
                transform: scale(0.8);
                opacity: 0.8;
            }}
        }}
        </style>
        """)
    ).add_to(m)

    # =========================
    # WEATHER IMPACT RADIUS
    # =========================
    radius = 4000 if temp > 30 else 2500

    folium.Circle(
        location=[lat, lon],
        radius=radius,
        color="#00f0ff",
        fill=True,
        fill_opacity=0.08
    ).add_to(m)

    # =========================
    # CONDITION LABEL 
    # =========================
    folium.Marker(
        [lat + 0.02, lon],
        icon=folium.DivIcon(html=f"""
        <div style="
            color:white;
            font-size:14px;
            text-shadow:0 0 10px #00f0ff;
        ">
        {condition.title()}
        </div>
        """)
    ).add_to(m)

    
    st.markdown("""
    <style>

    iframe {
        width: 100% !important;
        border-radius: 16px !important;
        background: transparent !important;
    }

    div[data-testid="stVerticalBlock"],
    div[data-testid="stHorizontalBlock"],
    .element-container {
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================
    # RENDER MAP 
    # =========================
    st_folium(m, width=None, height=450)


# =========================
# INPUT
# =========================
city = st.text_input("Enter City Name")

# =========================
# MAIN LOGIC 
# =========================
if city:

    # -------------------------
    # CURRENT WEATHER
    # -------------------------
    data = fetch_weather(city)

    if not data:
        st.error("Invalid city or API error")
        st.stop()

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    condition = data["weather"][0]["description"]

    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]

    apply_background(temp)

    # =========================
    # WEATHER
    # =========================
    st.subheader("Weather Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Temperature", f"{temp} °C")
    c2.metric("Humidity", f"{humidity} %")
    c3.metric("Wind", f"{wind} m/s")

    st.write(f"Condition: {condition}")

    # =========================
    # ALERTS
    # =========================
    st.subheader("Alerts")

    alerts = generate_alerts(data)

    if alerts:
        for a in alerts:
            st.warning(a)
    else:
        st.success("No alerts")

    # =========================
    # INSIGHT
    # =========================
    st.subheader("Insight")

    if temp <= 0:
        st.info("Freezing conditions")
    elif temp > 35:
        st.info("Extreme heat")
    else:
        st.info("Weather is stable")

    # =========================
    # MAP
    # =========================
    st.subheader("Weather Map")
    show_map(lat, lon, city, temp, condition)

    # =========================
    # REPORT
    # =========================
    st.subheader("Report")
    report = save_report(data, alerts)
    st.info(report)

    # =========================
    # FORECAST + ANALYTICS 
    # =========================
    st.subheader("Forecast & Analytics")

    forecast = fetch_forecast(city)

    if forecast:
        df = parse_forecast(forecast)

        st.dataframe(df, use_container_width=True)

        st.line_chart(df.set_index("datetime")[["temp", "humidity"]])

    else:
        st.warning("Forecast not available")