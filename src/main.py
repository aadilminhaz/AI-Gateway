from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health():
    return {"AI-Gateway is running!"}

