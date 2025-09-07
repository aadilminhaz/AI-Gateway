

def filterThinkFromResponse(response: str):
    llmResponse = response

    # Remove the <think> section if present
    if "<think>" in llmResponse and "</think>" in llmResponse:
        # Extract everything after </think>
        processedResponse = llmResponse.split("</think>")[-1].strip()
    else:
        processedResponse = llmResponse.strip()

    return processedResponse