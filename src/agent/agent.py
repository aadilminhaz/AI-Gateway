import ollama
from src.config.settings import system_prompt

target_model = 'llama3.2'


## Load the trained model
## Check for the prompt
def validate(prompt):

    response = ollama.chat(model=target_model,  messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}]
        )
    responseContent = response['message']['content']
    print("response : ", response)
    return responseContent
 