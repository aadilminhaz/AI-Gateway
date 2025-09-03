from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from huggingface_hub import login
from src.config.settings import settings

print ('Fine Tunning')

print('Logged in...')

login(token=settings.huggingface_key)

model_id="meta-llama/Llama-2-7b-chat-hf"


print("Loading Gemma model...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)
print("Successfully loaded model!")