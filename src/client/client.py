from openai import OpenAI
from src.config.settings import settings


client = OpenAI(api_key=settings.open_ai_key)
model = "gpt-5"

def inference(prompt: str) -> str:
    print('prompt', prompt)
    response = client.responses.create(
        model = model,
        input="Write a one-sentence instagram caption"
    )
    return response.output_text
