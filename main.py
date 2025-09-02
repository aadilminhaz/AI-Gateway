from fastapi import FastAPI, HTTPException
##from gateway.controller import gateway_router
from src.gateway.service import gateway_service
from src.config.settings import settings
from src.gateway.inferenceRequestModel import InferenceRequest


app = FastAPI()
#app.include_router(gateway_router)

@app.get("/")
def health():
    return {"message": "AI-Gateway is running!"}



@app.get("/inference")
def inference(inference_request: InferenceRequest):
    print('app-name : ', settings.app_name)
    #if (len(inference_request.) < 1):
    #    raise HTTPException(status_code=404, detail="Empty promt")
    return gateway_service(inference_request.prompt)
