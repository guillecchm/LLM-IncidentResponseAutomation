from google import genai
from google.genai import types

class Gemini():
    def __init__(self):
        self.client = genai.Client(api_key="")

    def send_prompt(self, model, prompt):
        response = self.client.models.generate_content(
            model=model,
            contents=prompt
        )

        return response
