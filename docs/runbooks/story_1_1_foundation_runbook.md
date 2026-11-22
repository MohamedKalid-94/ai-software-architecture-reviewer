## Filename

```text
docs/runbooks/story_1_1
_genai_platform_runbook.md

Purpose:
Documents:
- FastAPI startup
- Streamlit startup
- Expected output
- Troubleshooting

Content:
# Story 1.1 - Initialize Application Platform

## Objective
Create the application foundation:

- FastAPI backend
- Streamlit frontend
- Configuration management
- Logging
- Error handling


# Prerequisites

Python 3.12+

Virtual environment activated:

```bash
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run Backend
From project root:
uvicorn backend.app.main:app --reload

Expected:
Uvicorn running on http://127.0.0.1:8000
Application startup complete

Test:
Open:
http://127.0.0.1:8000

Expected:
{
 "application":"ArchAI Reviewer",
 "status":"running"
}

Swagger:
http://127.0.0.1:8000/docs

Run Frontend
Open another terminal:
cd frontend

Run:
streamlit run app.py

Expected:
Local URL:
http://localhost:8501

Story 1.1 Completion Criteria
✓ Backend running
✓ Frontend running
✓ Configuration loading
✓ Logging enabled
✓ Error middleware active
