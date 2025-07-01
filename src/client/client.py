##Client to call target model, with given promt and response with the response from the model
import httpx

BASE_URL = "http://localhost:8000"  # URL to call the target model endpoint

async def forward_request_to_my_api(endpoint: str, method="GET", payload=None):
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}{endpoint}"

        if method.upper() == "GET":
            response = await client.get(url)
        elif method.upper() == "POST":
            response = await client.post(url, json=payload)
        else:
            raise ValueError(f"Unsupported method: {method}")

        response.raise_for_status()
        return response.json()
