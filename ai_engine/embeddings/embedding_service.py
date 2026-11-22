"""
Embedding Service

Centralized embedding generation service.

Current Provider:
Ollama

Model:
nomic-embed-text
"""

from functools import lru_cache

from langchain_ollama import OllamaEmbeddings

from backend.app.config.settings import settings



@lru_cache(maxsize=1)
def get_embeddings():
    """
    Returns configured embedding model.
    """

    provider = settings.EMBEDDING_PROVIDER.lower()


    if provider == "ollama":

        return OllamaEmbeddings(
            model=settings.EMBEDDING_MODEL,
            base_url=settings.OLLAMA_BASE_URL
        )


    raise ValueError(
        f"Unsupported embedding provider: {provider}"
    )