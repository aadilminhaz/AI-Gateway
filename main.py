from fastapi import FastAPI, HTTPException, Depends
from src.gateway.service import gateway_service
from src.config.settings import settings
from src.gateway.inferenceModels import InferenceRequest, InferenceResponse


##from gateway.controller import gateway_router


app = FastAPI()
#app.include_router(gateway_router)

@app.get("/")
def health():
    return {"message": "AI-Gateway is running!"}



@app.get("/inference", response_model=InferenceResponse)
def inference(inference_request: InferenceRequest):
    #if (len(inference_request.) < 1):
    #    raise HTTPException(status_code=404, detail="Empty promt")
    response = gateway_service(inference_request)
    return InferenceResponse(response=response)


