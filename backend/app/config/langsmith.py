"""
LangSmith Configuration

Centralized AI observability setup.
"""


import os


def configure_langsmith():

    os.environ["LANGCHAIN_TRACING_V2"] = (
        "true"
    )


    os.environ["LANGCHAIN_API_KEY"] = (
        os.getenv("LANGSMITH_API_KEY", "")
    )


    os.environ["LANGCHAIN_PROJECT"] = (
        os.getenv(
            "LANGSMITH_PROJECT",
            "ArchAI Reviewer"
        )
    )


    return True