import streamlit as st
import requests


st.title(
    "ArchAI Reviewer"
)


st.subheader(
    "Enterprise AI Architecture Review Platform"
)


try:

    response = requests.get(
        "http://localhost:8000/health"
    )

    if response.status_code == 200:

        st.success(
            "Backend Connected"
        )

except Exception:

    st.error(
        "Backend Not Available"
    )


st.write(
    """
    Future capabilities:

    - Document Upload
    - RAG Analysis
    - AI Architecture Review
    - LangGraph Agents
    """
)