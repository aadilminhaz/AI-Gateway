# AI-Gateway
Multimodal AI Security: Mitigating prompt attack on AI Models using AI-Gateway

## Introduction
With immense boom of AI, most of the industries adopts or in the process of adopting AI. From Chat Bots to Risk/Fraud detection in FinTech, AI models are everywhere. But the rapid adoption and widespreading lansacpe of AI, increased the attack surface. Since AI applications are different from existing software systems, in terms of data usage, adaptibility, maintainance and security, the conventional ways of software security measures would not be sufficient to secure AI systems.
Among, different critical threats on AI, such as model hijacking, data vulnerability, etc, prompt-attack is the most curcial one.

This project introduces a AI-Gateway that puts a security layer over inference of AI models, the project validates the given input prompt for prompt-attack, it uses Custom trained Model to validate the input prompt before sending it for use to the AI model.

## Problem
Among various way to attack an ML/AI model, the prompt or input attacks are most effective and common because in order to serve a request model must interact and accept the input. The major problem in securing AI model is equipping the model with the capability to understand harmful/mallicious inputs in the form of text prompt, image or speech.

Currently a lot of research is going on training the models to idenitify harmful inputs to the model and make the model less velnurable. But this approach introduces challenges in terms of High-Cost, complexity and reliability in actual production environments. In order to do that, the model can be scanned by an AI security tools such as Mindguard then fine-tuned and retrained to idetify mallicious inputs to the model. But this approach has several challenges, the very first is adding overhead to the model to make it secure other than it's actual intended functionality, the other challenge arises when you have to secure multi-model architecture. For example if a system uses multiple AI agents, and all the models are independent of each other, it would be a redudant process to fine-tune and secure the models agains threatful inputs. Also in an enterprise, sometimes multiple models are in production to serve multiple clients, securing all the models in such manner would be extremely complex and expensive.

This proposal introduces an MultiModal AI-Gateway module, to intercept the inputs, validate them and safe-guard the models running without adding any overhead or re-training them, so that they can work as per their role. The proposal is based on API-Gateway design architechture, that is really popular in current micro-services architecture systems.


## Workflow
The project has two major components, API layer and a Validation model. The API layer intercepts the request from the user to the Model, and using Validation model it validates the given prompt from the user for mallicious input. The validation layer passes the request to the target model for inference if the given prompt is safe as inference input. If validation model finds the input prompt as treat in terms of vairous aspects of prompt-attack, it will block the request, safeguarding the target model.

For Core Validator Model, Llama 4 Scout will be used. The Llam model will be fine-tunned an custom trained to validate mallicious prompt. The first phase targets validation of mallicious text prompt, with the possibility to identify other form of mallicious prompt inputs.

## TO-DO:
Phase 0: Basic setup with an Interface that exposes AI-Gateway's API to recieve the user prompt, and forward it the the taget model by calling the target model inference API.
- Test the AI-Gateway API
- Connect the API to the service layer
- Sketch out Global Exception Handling and Logging
- Call Client layer from service layer, to foward the request to target model inference API

Phase 1: Model Implementation
- Basic model loading and inferencing
- Writing service layer to connect with model inferencing
- Connecting AI-Gateway to service, to vaidate the prompt


For fine-tuning the validation model, we need to find relavant dataset, here are some curation to find the required dataset:
- https://arxiv.org/abs/2402.13064



## Architecture

The project is divided into two major modules:
- AI-Gateway API layers
- Core Validator Model 

### AI-Gateway API layers
AI-Gateway has an exposed API, that intercepts the prompt to the target model and uses Core Valiator Model to check for mallicious prompts.

### Core Validator Model 
Llama 4 Scout Model will be used, custom trained and fine-tuned to validate a prompt for Mallicious context.
Using Sloth to train the Core model of AI-Gateway

## Result

This reseach assess vulnerablity of most popular open-source models using the openly available and synthetic datasets of halmful inputs, and then compares the result while using the proposed multimodal AI-Gateway layer over the models. The reseach focus on mallicious text and speech inputs but show the potential to do more work on visual inputs in the future.


## Conclusion
