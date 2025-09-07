import ollama
from src.config.settings import system_prompt
from src.utils.utils import filterThinkFromResponse

#target_model = 'llama3.2'
target_model = 'deepseek-r1'


## Load the trained model
## Check for the prompt
def validate(prompt):

    response = ollama.chat(model=target_model,  messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}]
        )
    responseContent = response['message']['content']
    responseContent = filterThinkFromResponse(responseContent)
    print("response : ", response)
    return responseContent
 