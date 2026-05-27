from gemini_config import model

class ReminderAgent:

    def create_reminder(self, text):

        prompt = f"""
        Create a short reminder for:

        {text}
        """

        response = model.generate_content(prompt)

        return response.text
