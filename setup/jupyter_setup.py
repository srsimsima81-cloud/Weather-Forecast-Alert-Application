import sys
import subprocess
from pathlib import Path
import nbformat as nbf

# =========================
# PATH SETUP (ROBUST)
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = BASE_DIR / "notebooks"


def install_dependencies():
    print("📦 Installing dependencies...")

    packages = ["jupyter", "ipykernel", "nbformat"]

    for pkg in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

    print("✅ Installed")


def setup_kernel():
    print("⚙️ Setting up kernel...")

    subprocess.check_call([
        sys.executable,
        "-m",
        "ipykernel",
        "install",
        "--user",
        "--name", "weathersphere_env",
        "--display-name", "Python (WeatherSphere)"
    ])

    print("✅ Kernel ready")


def create_folder():
    NOTEBOOKS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📁 Notebooks folder ready: {NOTEBOOKS_DIR}")


# =========================
# REAL NOTEBOOK CREATION
# =========================
def create_weather_notebook():

    print("📓 Creating real notebook with cells...")

    nb = nbf.v4.new_notebook()

    # ================= CELL 1 =================
    cell1 = nbf.v4.new_markdown_cell("""
# 🍃 WeatherSphere Notebook 🌀  
### Live Weather + Forecast Analysis System
""")

    # ================= CELL 2 =================
    cell2 = nbf.v4.new_code_cell("""
from src.weather_api import fetch_weather, fetch_forecast
from src.forecast import parse_forecast

print("Imports loaded ✔")
""")

    # ================= CELL 3 =================
    cell3 = nbf.v4.new_code_cell("""
city = "London"
data = fetch_weather(city)

data
""")

    # ================= CELL 4 =================
    cell4 = nbf.v4.new_code_cell("""
forecast = fetch_forecast("London")
df = parse_forecast(forecast)

df.head()
""")

    # ================= CELL 5 =================
    cell5 = nbf.v4.new_code_cell("""
import matplotlib.pyplot as plt

df.plot(x="datetime", y=["temp", "humidity"], figsize=(10,5))
plt.title("Weather Forecast Trend")
plt.show()
""")

    nb.cells = [cell1, cell2, cell3, cell4, cell5]

    file_path = NOTEBOOKS_DIR / "WeatherSphere.ipynb"

    with open(file_path, "w", encoding="utf-8") as f:
        nbf.write(nb, f)

    print(f"✅ Notebook created at: {file_path}")


# =========================
# FULL PIPELINE
# =========================
def full_setup():
    install_dependencies()
    setup_kernel()
    create_folder()
    create_weather_notebook()
    print("\n🚀 COMPLETE: Notebook is ready with prebuilt cells!")


if __name__ == "__main__":
    full_setup()