from langchain_openai import ChatOpenAI

from backend.ai.providers import LLMProvider
from backend.core.settings import settings


def get_llm():
    """
    Returns the configured LLM instance.
    """

    provider = settings.LLM_PROVIDER.lower()

    if provider == LLMProvider.OPENAI.value:
        return ChatOpenAI(
            model=settings.LLM_MODEL,
            temperature=settings.TEMPERATURE,
            max_tokens=settings.MAX_TOKENS,
            api_key=settings.OPENAI_API_KEY,
        )

    raise ValueError(f"Unsupported LLM provider: {provider}")