
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import yaml



with open("utils/prompt_templates.yaml", "r") as f:
    prompts = yaml.safe_load(f)

class TerminalAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.prompt = prompts['system_prompt'],
        self.model = "gemini-2.5-flash",

    def process(self, user_query):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction = self.prompt),
            contents=user_query
        )
        return response.text
    

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    terminal_agent = TerminalAgent(api_key)
    print(terminal_agent.process("Give me pandas installation command"))
