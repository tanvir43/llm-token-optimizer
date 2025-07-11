# Prompt Token Optimizer (Offline, Free)

A FastAPI-powered REST API to analyze and optimize LLM prompts for token usage — using only free, local tools.

## Features
- Token count using `tiktoken`
- Local prompt optimization using `llama3` via Ollama

## Getting Started

1. Install dependencies:

```yaml
pip install -r requirements.txt
```

2. Run Ollama in background:

```yaml
ollama run llama3
```

3. Start the FastAPI app:

```yaml
uvicorn app.main:app --reload
```