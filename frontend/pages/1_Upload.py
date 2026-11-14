import streamlit as st

st.title("📄 Upload Architecture Document")

uploaded_file = st.file_uploader(
    "Choose a PDF document",
    type=["pdf"],
)

if uploaded_file:
    st.success(f"{uploaded_file.name} uploaded successfully.")