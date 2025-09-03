from pydantic import BaseModel

class InferenceRequest(BaseModel):
    prompt: str
    targetId: str


class InferenceResponse(BaseModel):
    response: str


