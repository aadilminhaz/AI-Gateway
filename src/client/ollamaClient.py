import ollama

target_model = 'deepseek-r1'

def inference(prompt):
 response = ollama.chat(model=target_model, messages=[{"role": "user", "content": prompt}])
 responseContent = response['message']['content']
 return filterThinkFromResponse(responseContent)


def filterThinkFromResponse(response: str):
    llmResponse = response

    # Remove the <think> section if present
    if "<think>" in llmResponse and "</think>" in llmResponse:
        # Extract everything after </think>
        processedResponse = llmResponse.split("</think>")[-1].strip()
    else:
        processedResponse = llmResponse.strip()

    return processedResponse
