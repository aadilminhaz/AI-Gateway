from fastapi import FastAPI, HTTPException
##from gateway.controller import gateway_router
from src.gateway.service import gateway_service


app = FastAPI()
#app.include_router(gateway_router)

@app.get("/")
def health():
    return {"message": "AI-Gateway is running!"}



@app.get("/inference/{prompt}")
def inference(prompt: str):
    if (len(prompt) < 1):
        raise HTTPException(status_code=404, detail="Empty promt")
    return gateway_service(prompt)
