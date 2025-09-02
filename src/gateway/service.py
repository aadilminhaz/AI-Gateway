#from src.client.client import inference
from src.client.ollamaClient import inference
from src.agent.validatorAgent import validatePrompt
from fastapi import HTTPException

def gateway_service(prompt: str) -> str:
    #call validator Model

    if (call_validator(prompt = prompt) == False):
        return {"message" : "Mallicious Input"}
    
    ##call target model client
    return call_target_model(prompt=prompt)


def call_validator(prompt: str) -> bool:
    ## call validator model
    ## create an ollama client to validator model
    return validatePrompt(prompt=prompt)

def call_target_model(prompt: str):
    ##create an ollama client to target model   
    ##return {"message" : "response from target model"}
    try:
        return inference(prompt=prompt)
        #return {"message" : "Sample response from Target LLM"}
    except:
        raise HTTPException(status_code=500, detail="Exception from Target Model")
    


