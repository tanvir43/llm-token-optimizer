from fastapi import APIRouter
from app.schemas import PromptInput, CompareOutput
from app.services.tokenizer import count_tokens
from app.services.optimizer import optimize_prompt

router = APIRouter()

@router.post("/analyze")
def analyze(data: PromptInput):
    tokens = count_tokens(data.prompt)
    return {"tokens": tokens}

@router.post("/optimize")
def optimize(data: PromptInput):
    optimized = optimize_prompt(data.prompt)
    return {"optimized_prompt": optimized}

@router.post("/compare", response_model=CompareOutput)
def compare(data: PromptInput):
    original_tokens = count_tokens(data.prompt)
    optimized = optimize_prompt(data.prompt)
    optimized_tokens = count_tokens(optimized)
    savings = original_tokens - optimized_tokens

    return CompareOutput(
        original_prompt=data.prompt,
        optimized_prompt=optimized,
        original_tokens=original_tokens,
        optimized_tokens=optimized_tokens,
        token_savings=savings
    )
