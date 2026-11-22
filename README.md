# ArchAI Reviewer

## Enterprise AI Architecture Review Platform

An AI-powered software architecture review platform that analyzes architecture artifacts using:

- LangChain
- LangGraph multi-agent workflows
- RAG-based knowledge retrieval
- LangSmith observability
- AI evaluation pipelines

The platform generates evidence-backed architecture recommendations for software teams.

---

# Current Development Status

## Milestone 1 — AI Platform Foundation

### Completed Stories

| Story | Description | Status |
|---|---|---|
| Story 1.1 | Initialize Application Platform | ✅ Completed |
| Story 1.2 | Configure GenAI Platform | ✅ Completed |

---

# Story 1.2 — Configure GenAI Platform

## Objective

Establish the GenAI foundation required for future:

- RAG pipeline
- LangGraph agents
- AI evaluation
- Architecture review workflows


---

# Implemented Components

## 1. LLM Service Layer

### Technology

- LangChain
- Ollama
- qwen2.5:3b


### Architecture

```
Application
     |
     |
LLM Service Wrapper
     |
     |
LangChain
     |
     |
Ollama Runtime
     |
     |
qwen2.5:3b
```


Responsibilities:

- Centralized LLM access
- Provider abstraction
- Model configuration management
- Temperature control
- Token configuration


---

# 2. Embedding Service Layer

### Technology

- LangChain
- Ollama Embeddings
- nomic-embed-text


### Architecture

```
Documents
    |
    |
Embedding Service
    |
    |
LangChain
    |
    |
Ollama Embedding Model
    |
    |
nomic-embed-text
```


Responsibilities:

- Generate document embeddings
- Prepare future RAG integration
- Maintain embedding provider abstraction


---

# 3. Configuration Management

## Environment Configuration

Centralized configuration through:

```
.env
```

Configured:

```
Application Settings
Logging Settings
Backend Settings
LLM Settings
Embedding Settings
LangSmith Settings
```


Example:

```env
LLM_PROVIDER=ollama
LLM_MODEL=qwen2.5:3b

EMBEDDING_PROVIDER=ollama
EMBEDDING_MODEL=nomic-embed-text

OLLAMA_BASE_URL=http://localhost:11434
```

---

# 4. LangSmith Observability Foundation

## Purpose

Enable visibility into AI execution.


Configured capabilities:

- LLM tracing
- Prompt tracking
- Execution monitoring
- Future agent tracing
- Evaluation integration


Architecture:

```
LangChain Application

        |

     LangSmith

        |

Trace
Prompt
Latency
Token Usage
Evaluation
```

---

# 5. AI Platform Validation

Created automated validation:

Location:

```
ai_engine/validation/ai_platform_check.py
```


Run:

```bash
python -m ai_engine.validation.ai_platform_check
```


Validation checks:

```
✓ Configuration loading

✓ Ollama connectivity

✓ LLM invocation

✓ Embedding generation

✓ LangSmith configuration
```


Expected:

```
ArchAI Reviewer - AI Platform Validation

✓ Configuration loaded

✓ LLM connection successful

✓ Embedding generation successful

✓ LangSmith tracing enabled


AI Platform Ready
```

---

# Current AI Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Frontend | Streamlit |
| LLM Framework | LangChain |
| LLM Runtime | Ollama |
| LLM Model | qwen2.5:3b |
| Embedding Model | nomic-embed-text |
| Observability | LangSmith |
| Configuration | Pydantic Settings |
| Language | Python 3.12 |

---

# Project Structure (Current)

```
ai-software-architecture-reviewer

├── backend
│   └── app
│       ├── config
│       │   ├── settings.py
│       │   └── langsmith.py
│       └── main.py
│
├── ai_engine
│   ├── llm
│   │   └── llm_service.py
│   │
│   ├── embeddings
│   │   └── embedding_service.py
│   │
│   └── validation
│       ├── test_llm.py
│       ├── test_embeddings.py
│       └── ai_platform_check.py
│
├── frontend
│
├── docs
│   └── runbooks
│
├── .env
├── requirements.txt
└── README.md
```

---

# Running the Application

## Backend

```bash
uvicorn backend.app.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```


## Frontend

```bash
streamlit run frontend/app.py
```


---

# Next Development Phase

## Story 1.3 — Define Core Data Models

Next implementation:

Domain models:

```
Project

Document

Review

Finding

EvaluationResult
```

These models will support:

- Document intelligence
- RAG pipeline
- LangGraph workflow
- Human approval process
- AI evaluation system

---

# Architecture Evolution Roadmap

Current:

```
FastAPI
   |
LangChain
   |
Ollama
   |
LangSmith
```

Future:

```
User
 |
FastAPI
 |
Review Management
 |
LangGraph Supervisor
 |
Multi-Agent Review System
 |
RAG Knowledge Engine
 |
Evidence Layer
 |
Human Approval
 |
Evaluation Pipeline
```