# AI-Gateway
AI Security: Mitigating prompt attack on AI Models using AI-Gateway

## Introduction
With immense boom of AI, most of the industries adopts or in the process of adopting AI. From Chat Bots to Risk/Fraud detection in FinTech, AI models are everywhere. But the rapid adoption and widespreading lansacpe of AI, increased the attack surface. Since AI applications are different from existing software systems, in terms of data usage, adaptibility, maintainance and security, the conventional ways of software security measures would not be sufficient to secure AI systems.
Among, different critical threats on AI, such as model hijacking, data vulnerability, etc, prompt-attack is the most curcial one.
This project introduces a AI-Gateway that puts a security layer over inference of AI models, the project validates the given input prompt for prompt-attack, it uses Custom trained Model to validate the input prompt before sending it for use to the AI model.

## Workflow
The project has two major components, API layer and a Validation model. The API layer intercepts the request from the user to the Model, and using Validation model it validates the given prompt from the user for mallicious input. The validation layer passes the request to the target model for inference if the given prompt is safe as inference input. If validation model finds the input prompt as treat in terms of vairous aspects of prompt-attack, it will block the request, safeguarding the target model.

For Core Validator Model, Llama 4 Scout will be used. The Llam model will be fine-tunned an custom trained to validate mallicious prompt. The first phase targets validation of mallicious text prompt, with the possibility to identify other form of mallicious prompt inputs.

TO-DO:
Phase 0: Basic setup with an Interface that exposes AI-Gateway's API to recieve the user prompt, and forward it the the taget model by calling the target model inference API.
- Test the AI-Gateway API
- Connect the API to the service layer
- Sketch out Global Exception Handling and Logging
- Call Client layer from service layer, to foward the request to target model inference API



## Architecture

The project is divided into two major modules:
- AI-Gateway API layers
- Core Validator Model 

### AI-Gateway API layers
AI-Gateway has an exposed API, that intercepts the prompt to the target model and uses Core Valiator Model to check for mallicious prompts.

### Core Validator Model 
Llama 4 Scout Model will be used, custom trained and fine-tuned to validate a prompt for Mallicious context.
Using Sloth to train the Core model of AI-Gateway

## 

## Conclusion
