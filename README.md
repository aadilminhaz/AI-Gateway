# AI-Gateway
AI Security: Mitigating prompt attack on AI Models using AI-Gateway

## Introduction
With immense boom of AI, most of the industries adopts or in the process of adopting AI. From Chat Bots to Risk/Fraud detection in FinTech, AI models are everywhere. But the rapid adoption and widespreading lansacpe of AI, increased the attack surface. Since AI applications are different from existing software systems, in terms of data usage, adaptibility, maintainance and security, the conventional ways of software security measures would not be sufficient to secure AI systems.
Among, different critical threats on AI, such as model hijacking, data vulnerability, etc, prompt-attack is the most curcial one.
This project introduces a AI-Gateway that puts a security layer over inference of AI models, the project validates the given input prompt for prompt-attack, it uses Custom trained Model to validate the input prompt before sending it for use to the AI model.

## Workflow
The project has two major components, API layer and a Validation model. The API layer intercepts the request from the user to the Model, and using Validation model it validates the given prompt from the user for mallicious input. The validation layer passes the request to the target model for inference if the given prompt is safe as inference input. If validation model finds the input prompt as treat in terms of vairous aspects of prompt-attack, it will block the request, safeguarding the target model.


## Architecture

The project is divided into two major modules:
- AI-Gateway API layers
- Validator Model

## 

## Conclusion
