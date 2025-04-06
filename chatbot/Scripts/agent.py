# agents.py

import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # 🔑 replace with real key

class WeatherAgent:
    @staticmethod
    def get_weather(city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return {"error": "City not found"}

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }

class CropPredictionAgent:
    @staticmethod
    def predict_crop(soil_type, region):
        # Dummy logic — real ML model laga sakta hai
        if soil_type == "loamy" and region == "Punjab":
            return "Best crop: Wheat"
        return "Try Rice or Maize based on climate."

class FertilizerAgent:
    @staticmethod
    def recommend_fertilizer(crop, soil_type):
        # Dummy logic
        if crop.lower() == "wheat" and soil_type == "loamy":
            return "Recommended fertilizer: Urea + DAP"
        return "Use balanced NPK fertilizer."
