# ArchAI Reviewer

## Enterprise AI Architecture Review Platform

An AI-powered software architecture review platform that analyzes architecture artifacts using:

- LangChain
- LangGraph multi-agent workflows
- RAG-based retrieval
- LangSmith observability
- AI evaluation pipelines

The platform generates evidence-backed architecture recommendations.

---

# Current Development Status

## Milestone 1 — AI Platform Foundation

**Status: Completed ✅**

Objective:

Establish the application foundation, AI connectivity, configuration management, and domain contracts.

---

# Completed Stories

| Story | Description | Status |
|---|---|---|
| Story 1.1 | Initialize Application Platform | ✅ Completed |
| Story 1.2 | Configure GenAI Platform | ✅ Completed |
| Story 1.3 | Define Core Data Models | ✅ Completed |

---

# Story 1.1 — Initialize Application Platform

Implemented:

✅ FastAPI backend foundation  
✅ Streamlit frontend foundation  
✅ Project structure  
✅ Environment configuration  
✅ Logging framework  
✅ Configuration management  
✅ Error handling foundation  


Backend execution:

```bash
uvicorn backend.app.main:app --reload
```


Frontend execution:

```bash
streamlit run frontend/app.py
```

---

# Story 1.2 — Configure GenAI Platform

Implemented:

## LLM Integration

Technology:

- LangChain
- Ollama
- qwen2.5:3b


## Embedding Integration

Technology:

- Ollama Embeddings
- nomic-embed-text


## Observability

Technology:

- LangSmith


Capabilities:

- LLM tracing
- Prompt monitoring
- Execution tracking

---

# Story 1.3 — Define Core Data Models

Implemented domain foundation for future AI workflows.

## Domain Models

Created:

```
Project
Document
Review
Finding
Evaluation
```

Location:

```
backend/app/models
```

---

## API Schemas

Created:

```
ProjectSchema
DocumentSchema
ReviewSchema
FindingSchema
EvaluationSchema
```

Location:

```
backend/app/schemas
```

---

## Validation

Completed:

✅ Model validation  
✅ Schema validation  
✅ Import integration testing  


Validation result:

```
Models imported successfully ✅
Schemas imported successfully ✅
```

---

# Current Architecture Foundation

```
                    ArchAI Reviewer

                           |
                           |

                    FastAPI Backend

                           |

        +------------------+------------------+

        |                                     |

   AI Platform Layer                  Domain Layer

        |                                     |

 LangChain + Ollama                 Models + Schemas

        |

 LangSmith Observability

```

---

# Technology Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Frontend | Streamlit |
| Language | Python 3.12 |
| LLM Framework | LangChain |
| LLM Runtime | Ollama |
| LLM Model | qwen2.5:3b |
| Embedding Model | nomic-embed-text |
| Observability | LangSmith |
| Validation | Pydantic |

---

# Next Milestone

## Milestone 2 — Document Intelligence & Evidence Layer

Objective:

Build trusted document understanding capabilities.

Upcoming:

- Document upload API
- Document validation
- PDF processing
- Metadata extraction
- Evidence management

Next Story:

**Story 2.1 — Document Upload System**
```
Upload API
    |
Document Validation
    |
Metadata Generation
    |
Document Storage
```