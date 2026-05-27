from agents.weather_agent import WeatherAgent
from agents.reminder_agent import ReminderAgent
import json
import os

class CoordinatorAgent:

    def __init__(self):

        self.weather_agent = WeatherAgent()

        self.reminder_agent = ReminderAgent()

    def process(self, user_input):

        responses = []

        user_input_lower = user_input.lower()

        if "weather" in user_input_lower:

            weather_response = self.weather_agent.analyze_weather(
                "Kochi"
            )

            responses.append(weather_response)

        if "remind" in user_input_lower:

            reminder_response = self.reminder_agent.create_reminder(
                user_input
            )

            responses.append(reminder_response)

        self.save_memory(user_input)

        return responses

    def save_memory(self, message):

        memory_data = {
            "last_message": message
        }

        # Resolve path to backend directory dynamically
        backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        memory_path = os.path.join(backend_dir, "memory.json")

        with open(memory_path, "w") as file:

            json.dump(memory_data, file)

