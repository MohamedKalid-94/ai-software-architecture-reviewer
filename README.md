# ArchAI Reviewer

## Enterprise AI Architecture Review Platform

An AI-powered software architecture review platform that analyzes architecture artifacts using:

- LangChain
- LangGraph multi-agent workflows
- RAG-based retrieval
- LangSmith observability
- AI evaluation pipelines

The platform generates evidence-backed architecture recommendations with source traceability.

---

# Development Status

## Milestone 1 — AI Platform Foundation

**Status: Completed ✅**

## Objective

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

## Implemented

✅ FastAPI backend foundation  
✅ Streamlit frontend foundation  
✅ Project structure  
✅ Python virtual environment  
✅ Environment configuration  
✅ Settings management  
✅ Structured logging  
✅ Error handling middleware  

## Backend Execution

```bash
uvicorn backend.app.main:app --reload

## Frontend Execution
streamlit run frontend/app.py

# Story 1.2 — Configure GenAI Platform
LLM Integration
Technology:
- LangChain
- Ollama
- qwen2.5:3b

Embedding Integration
Technology:
- Ollama Embeddings
- nomic-embed-text

Observability
Technology:
- LangSmith

Capabilities:
- LLM tracing
- Prompt execution monitoring
- AI workflow observability

Story 1.3 — Define Core Data Models
Domain Models
Created:
Project
Document
Review
Finding
Evaluation

Location:
backend/app/models

API Schemas
Created:
ProjectSchema
DocumentSchema
ReviewSchema
FindingSchema
EvaluationSchema

Location:
backend/app/schemas

Validation
Completed:
Models imported successfully ✅
Schemas imported successfully ✅

Milestone 2 — Document Intelligence & Evidence Layer
Status: Completed ✅
Objective
Build trusted document understanding with evidence references.
Completed Stories
Story	Description	Status
Story 2.1	Document Upload System	✅ Completed
Story 2.2	Document Intelligence Pipeline	✅ Completed
Story 2.3	Evidence Management System	✅ Completed


Story 2.1 — Document Upload System
Implemented
✅ Document upload API
✅ PDF validation
✅ File type validation
✅ File size validation
✅ Document storage
✅ Metadata generation
✅ Upload status tracking  
Capabilities
The system can:
- Accept architecture documents
- Validate uploaded files
- Store documents securely
- Generate document metadata
Story 2.2 — Document Intelligence Pipeline
Implemented
✅ PDF parsing
✅ Page extraction
✅ Heading extraction
✅ Section detection
✅ Document classification
✅ Metadata extraction  
Capabilities
The system can:
- Extract document content
- Preserve document structure
- Identify sections
- Prepare documents for evidence creation
Story 2.3 — Evidence Management System
Implemented
✅ Evidence domain model
✅ Evidence schema
✅ Source reference tracking
✅ Evidence retrieval
✅ Citation generation
✅ Source linking foundation  
Evidence Schema
{
    "document":"",
    "page":"",
    "section":"",
    "content":""
}

Example Evidence Record
{
    "document":"architecture.pdf",
    "page":"12",
    "section":"Database Architecture",
    "content":"Database does not have replication configured"
}

Validation
Evidence validation passed ✅

Current Architecture Foundation
                    ArchAI Reviewer


                          |

                  FastAPI Backend


                          |

        +-----------------+-----------------+

        |                                   |

Document Intelligence              AI Platform Layer

        |                                   |

Evidence Management              LangChain + Ollama

                                            |

                                      LangSmith



Technology Stack
Layer	Technology
Backend	FastAPI
Frontend	Streamlit
Language	Python 3.12
LLM Framework	LangChain
Agent Framework	LangGraph
LLM Runtime	Ollama
LLM Model	qwen2.5:3b
Embedding Model	nomic-embed-text
Observability	LangSmith
Validation	Pydantic


Upcoming Milestone
Milestone 3 — Enterprise RAG Pipeline
Status: Planned 🚧
Objective
Build accurate knowledge retrieval for architecture review workflows.
Planned Stories
Story	Description
Story 3.1	Build Embedding Pipeline
Story 3.2	Implement Hybrid Retrieval
Story 3.3	Implement Reranking
Story 3.4	Context Optimization


Development Roadmap
Milestone 1
AI Platform Foundation
        |
        | ✅ Completed
        |
Milestone 2
Document Intelligence & Evidence Layer
        |
        | ✅ Completed
        |
Milestone 3
Enterprise RAG Pipeline
        |
        | 🚧 Planned
        |
Milestone 4
Multi-Agent Architecture Review

Project Vision
ArchAI Reviewer will evolve into an enterprise AI architecture review platform capable of:
- Understanding architecture documents
- Retrieving relevant engineering knowledge
- Producing evidence-backed findings
- Providing architecture improvement recommendations
- Supporting multi-agent AI review workflows