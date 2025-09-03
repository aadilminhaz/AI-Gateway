from src.client.ollamaClient import inference
from src.agent.validatorAgent import validatePrompt
from src.gateway.inferenceModels import InferenceRequest
from fastapi import HTTPException

def gateway_service(inferenceRequest: InferenceRequest) -> str:
    #call validator Model
    if (call_validator(prompt = inferenceRequest.prompt) == False):
        raise HTTPException(status_code=400, detail="Mallicious Input to LLM")
    
    ##call target model client
    return call_target_model(prompt= inferenceRequest.prompt)


def call_validator(prompt: str) -> bool:
    return validatePrompt(prompt=prompt)

def call_target_model(prompt: str):
    ##create an ollama client to target model   
    try:
        print('promt to target model : ', prompt)
        return inference(prompt=prompt)
        #return "Sample response from Target LLM"
    except:
        raise HTTPException(status_code=500, detail="Exception from Target Model")
    


