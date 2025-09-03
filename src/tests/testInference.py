import requests
from src.config.settings import settings

url = "http://127.0.0.1:8000/inference"
payload = {
    "prompt": "what is the capital of Spain",
    "targetId": "ollama"
}

#if we want to take api-key in the json
headers = {'x-api-key': settings.open_ai_key, "Content-Type": "application/json"}

response = requests.post(url, data=payload, headers=headers)
print(response.json())