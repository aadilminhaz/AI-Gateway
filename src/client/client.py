from openai import OpenAI


client = OpenAI(api_key="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")
model = "gpt-5"

def inference(prompt: str) -> str:
    print('prompt', prompt)
    response = client.responses.create(
        model = model,
        input="Write a one-sentence instagram caption"
    )
    return response.output_text
