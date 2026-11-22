"""
ArchAI Reviewer - AI Platform Validation

Validates:
- Configuration
- LLM connectivity
- Embedding generation
- LangSmith configuration
"""


from backend.app.config.settings import settings
from ai_engine.llm import get_llm
from ai_engine.embeddings import get_embeddings



def check_configuration():

    print("\n[1] Checking configuration...")

    print(f"Application : {settings.APP_NAME}")
    print(f"Environment : {settings.ENVIRONMENT}")
    print(f"LLM Model   : {settings.LLM_MODEL}")
    print(f"Embedding   : {settings.EMBEDDING_MODEL}")

    print("✓ Configuration loaded")



def check_llm():

    print("\n[2] Checking LLM connection...")

    llm = get_llm()

    response = llm.invoke(
        "Explain software architecture in one sentence."
    )

    print("LLM Response:")
    print(response.content)

    print("✓ LLM connection successful")



def check_embeddings():

    print("\n[3] Checking embedding service...")

    embeddings = get_embeddings()

    vector = embeddings.embed_query(
        "ArchAI Reviewer analyzes software architecture."
    )

    print(
        f"Embedding dimension: {len(vector)}"
    )

    print("✓ Embedding generation successful")



def check_langsmith():

    print("\n[4] Checking LangSmith configuration...")

    if settings.LANGSMITH_TRACING:

        print(
            "✓ LangSmith tracing enabled"
        )

    else:

        print(
            "⚠ LangSmith tracing disabled"
        )



def main():

    print("=" * 60)
    print("ArchAI Reviewer - AI Platform Validation")
    print("=" * 60)


    check_configuration()

    check_llm()

    check_embeddings()

    check_langsmith()


    print("\n" + "=" * 60)
    print("AI Platform Ready ✅")
    print("=" * 60)



if __name__ == "__main__":
    main()