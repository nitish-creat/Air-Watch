import requests
import pandas as pd
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")

# Use fixed cities (important for consistency)
cities = ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Chandigarh"]

weather_data = []
aqi_data = []

# ---------------- WEATHER DATA ----------------
for city in cities:
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()

        weather_data.append({
            "city": city,
            "temperature": response["main"]["temp"],
            "humidity": response["main"]["humidity"],
            "wind_speed": response["wind"]["speed"],
            "pressure": response["main"]["pressure"]
        })

    except Exception as e:
        print(f"Weather API error for {city}: {e}")

# ---------------- AQI DATA ----------------
for city in cities:
    try:
        url = f"https://api.waqi.info/feed/{city}/?token={TOKEN}"
        response = requests.get(url).json()

        if response["status"] == "ok":
            data = response["data"]

            aqi_data.append({
                "city": city,
                "aqi": data.get("aqi"),
                "pm25": data.get("iaqi", {}).get("pm25", {}).get("v"),
                "pm10": data.get("iaqi", {}).get("pm10", {}).get("v")
            })
        else:
            print(f"AQI API error for {city}: {response['data']}")

    except Exception as e:
        print(f"AQI exception for {city}: {e}")

# ---------------- MERGE DATA ----------------
weather_df = pd.DataFrame(weather_data)
aqi_df = pd.DataFrame(aqi_data)

df = pd.merge(weather_df, aqi_df, on="city")

# Add full timestamp
df["timestamp"] = datetime.now()

# ---------------- SAVE DATA ----------------

# Save CSV (relative path - professional way)
csv_path = "data/raw/raw_data.csv"
os.makedirs("data/raw", exist_ok=True)

if not os.path.exists(csv_path):
    df.to_csv(csv_path, index=False)
else:
    df.to_csv(csv_path, mode="a", header=False, index=False)

# Save to SQLite
db_path = "database/airwatch.db"
os.makedirs("database", exist_ok=True)

conn = sqlite3.connect(db_path)
df.to_sql("air_quality", conn, if_exists="append", index=False)
conn.close()

print("✅ Data fetched and stored successfully!")