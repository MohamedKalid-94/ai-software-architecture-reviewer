import streamlit as st
from services.api import check_backend_health

st.set_page_config(
    page_title="AI Software Architecture Reviewer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🤖 AI Software Architecture Reviewer")

st.markdown("""
Welcome to the AI Software Architecture Reviewer.

This application analyzes software architecture documents using:

- LangChain
- LangGraph
- LangSmith
- AI Evaluations
""")

col1, col2, col3 = st.columns(3)

col1.metric("Project", "Ready")
col2.metric("Backend", "Connected")
col3.metric("Version", "0.1.0")

try:
    backend = check_backend_health()
    st.success(f"Backend Status: {backend['status']}")
except Exception:
    st.error("Backend is not running.")