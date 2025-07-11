from pydantic import BaseModel

class PromptInput(BaseModel):
    prompt: str

class CompareOutput(BaseModel):
    original_prompt: str
    optimized_prompt: str
    original_tokens: int
    optimized_tokens: int
    token_savings: int