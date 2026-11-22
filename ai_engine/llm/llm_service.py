"""
Central LLM Service

Supports configurable LLM providers.
Current provider:
Ollama
"""

from functools import lru_cache

from langchain_ollama import ChatOllama

from backend.app.config.settings import settings



@lru_cache(maxsize=1)
def get_llm():

    provider = settings.LLM_PROVIDER.lower()


    if provider == "ollama":

        return ChatOllama(
            model=settings.LLM_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=settings.LLM_TEMPERATURE,
        )


    raise ValueError(
        f"Unsupported LLM provider: {provider}"
    )