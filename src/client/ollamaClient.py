import ollama

target_model = 'deepseek-r1'

    
def inference(prompt):
    response = ollama.generate(model=target_model, prompt=prompt)
    print(response['response'])
    full_response = response['response']

    # Remove the <think> section if present
    if "<think>" in full_response and "</think>" in full_response:
        # Extract everything after </think>
        final_response = full_response.split("</think>")[-1].strip()
    else:
        final_response = full_response.strip()

    
    return final_response



