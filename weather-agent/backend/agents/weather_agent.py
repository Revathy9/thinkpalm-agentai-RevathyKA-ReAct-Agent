from tools.weather_tool import get_weather
from gemini_config import model

class WeatherAgent:

    def analyze_weather(self, city):

        weather = get_weather(city)

        prompt = f"""
        Analyze this weather information.

        Weather Data:
        {weather}

        Give:
        1. Weather Summary
        2. Safety Advice
        """

        response = model.generate_content(prompt)

        return response.text
