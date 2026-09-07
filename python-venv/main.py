import requests
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Get the city name from .env, or use a default
city = os.getenv("CITY", "Phnom Penh")

print(f"Checking weather for: {city}")
print("-" * 30)

# response = requests.get(f"https://wttr.in/{city}?format=3")
response = requests.get(f"https://wttr.in/{city}")

print(response.text)