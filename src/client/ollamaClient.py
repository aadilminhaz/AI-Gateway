import ollama

target_model = 'llama2'

    
def call_target_model(prompt):
    response = ollama.generate(model=target_model, prompt=prompt)
    print(response['response'])

#call_target_model('What is capital of Japan')


