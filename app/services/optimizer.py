import requests

def optimize_prompt(prompt: str) -> str:
    ollama_url = "http://localhost:11434/api/generate"
    system_prompt = (
        "You are a prompt rewriter. Rewrite the given prompt to preserve its meaning "
        "while using fewer words and tokens. Be concise and clear."
    )
    
    payload = {
        "model": "llama3",
        "prompt": f"{system_prompt}\nPrompt: {prompt}\nShortened:",
        "stream": False
    }

    try:
        response = requests.post(ollama_url, json=payload, timeout=10)
        result = response.json()
        return result.get("response", "").strip()
    except Exception as e:
        return f"[Error: {str(e)}]"
