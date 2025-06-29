from google import genai
from google.genai import types
from src.agent import TerminalAgent
import sys
import subprocess



from dotenv import load_dotenv
import os

if len(sys.argv) > 1:
    user_query = " ".join(sys.argv[1:])
else:
    raise Exception("Please provide your input")


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
# ...existing code...

exit = False

terminal_agent = TerminalAgent(api_key)


response = terminal_agent.process(user_query)

print(f"COMMAND - {response}")

exec = input("Do you want to execute this command Y/N - ")

print("\n")
if exec.lower() == "y":
    result = subprocess.run(response, shell=True, capture_output=True, text=True)
    print(result.stdout)


print(response)


