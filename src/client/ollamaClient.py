import ollama
from src.utils.utils import filterThinkFromResponse

target_model = 'deepseek-r1'

def inference(prompt):
 response = ollama.chat(model=target_model, messages=[{"role": "user", "content": prompt}])
 responseContent = response['message']['content']
 return filterThinkFromResponse(responseContent)
