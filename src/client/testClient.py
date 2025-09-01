from ollamaClient import call_target_model
import httpx
import ollama

target_model = 'llama2'

async def forward_request_to_my_api(endpoint: str, method="GET", payload=None):
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}{endpoint}"

        if method.upper() == "GET":
            #response = await client.get(url)
            response = await ollama.generate(model=target_model, prompt=payload)
        else:
            raise ValueError(f"Unsupported method: {method}")

        response.raise_for_status()
        return response.json()