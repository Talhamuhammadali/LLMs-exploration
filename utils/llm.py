"""LLMs available to use for agents."""
import os
from openai import OpenAI

def get_llm(provider: str = "openai", model: str = "gpt-5-mini"):
    """Get the llm from the requested provider"""
    if provider == "openai":    
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    else:
        raise ValueError("Not Supported model provider")
    return client