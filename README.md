<<<<<<< HEAD
# ArchAI Reviewer

Enterprise AI Architecture Review Platform

## Current Status

Milestone 1 - Foundation

---

# Development Setup

ArchAI Reviewer uses a monorepo structure with:

- FastAPI backend
- Streamlit frontend
- Shared root configuration

Project structure:

ai-software-architecture-reviewer/

├── backend/
│   └── app/
│
├── frontend/
│   └── app.py
│
├── .env
├── requirements.txt
└── README.md

---

# Run Backend

Open Terminal 1.

From project root:


uvicorn backend.app.main:app --reload

Backend runs at:


http://127.0.0.1:8000

Health check:


http://127.0.0.1:8000

Expected response:

```json
{
  "application": "ArchAI Reviewer",
  "version": "1.0.0",
  "status": "running"
}

Run Frontend
Open Terminal 2.

From project root:
streamlit run frontend/app.py

Frontend runs at:
http://localhost:8501

The Streamlit application connects with the FastAPI backend.
Environment Configuration
ArchAI Reviewer uses a shared root environment configuration.

Create:
.env

Example:
APP_NAME=ArchAI Reviewer
APP_VERSION=1.0.0
ENVIRONMENT=development

BACKEND_URL=http://127.0.0.1:8000

Frontend Backend Configuration
The frontend should read the backend URL from .env.

Development:
BACKEND_URL=http://127.0.0.1:8000

Production:
BACKEND_URL=https://api.archai-reviewer.com

The application can switch environments without changing source code.
Current Milestone
Milestone 1 - Foundation
Completed:

✅ FastAPI backend setup
✅ Streamlit frontend setup
✅ Root environment configuration
✅ Logging framework
✅ Configuration management
✅ Error handling middleware  
=======
# AI Software Architecture Reviewer

An Enterprise-grade AI application that reviews Software Architecture Documents using:

- LangChain
- LangGraph
- LangSmith
- Retrieval-Augmented Generation (RAG)
- AI Evaluations

## Features

- Multi-Agent Architecture Review
- Document Intelligence
- Architecture Quality Analysis
- Security Review
- Performance Review
- API Design Review
- LangSmith Observability
- AI Evaluations

## Technology Stack

- Python
- FastAPI
- Streamlit
- LangChain
- LangGraph
- LangSmith
- ChromaDB

## Project Status

🚧 Milestone 1 – Foundation (In Progress)
>>>>>>> b166cd258ae12270b896eb51117873cbb952c280
