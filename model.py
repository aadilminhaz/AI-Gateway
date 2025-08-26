from transformers import pipeline
import torch
from huggingface_hub import login

login(token="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") 

model_id = "meta-llama/Llama-4-Scout-17B-16E"

pipe = pipeline(
    "text-generation",
    model=model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16,
)

output = pipe("Roses are red,", max_new_tokens=200)
