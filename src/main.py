from fastapi import FastAPI
from gateway.controller import gateway_router

app = FastAPI()
app.include_router(gateway_router)

@app.get("/")
async def health():
    return {"AI-Gateway is running!"}

