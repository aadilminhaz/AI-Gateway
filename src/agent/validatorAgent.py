from src.agent.agent import validate


## determine true or false from the output of the output of the validator model
def validatePrompt(prompt: str) -> bool:
    
    validationResponse = validate(prompt=prompt)
    print("validation Response : ", validationResponse)
    isValid = string_to_boolean(validationResponse)
    print('isValid : ', isValid)
    return isValid

def string_to_boolean(input: str):
    return input.lower() in ['true', "True.", "True", "true."]