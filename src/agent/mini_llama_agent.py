from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from huggingface_hub import login

print ('Fine Tunning')

print('Logged in...')

# Gemma 2B model (small and efficient)
#model_id = "google/gemma-2b-it"
#model_id = "meta-llama/Llama-4-Scout-17B-16E"
model_id="meta-llama/Llama-2-7b-chat-hf"


print("Loading Gemma model...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)
print("Successfully loaded model!")