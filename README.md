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

# Milestone 2 — Document Intelligence & Evidence Layer

**Status:** 🚧 In Progress

## Story 2.1 — Document Upload System

**Status:** ✅ Completed

### Objective

Provide a secure document upload pipeline that validates, stores, and prepares architecture documents for future AI processing.

### Features Implemented

- Document Upload API
- PDF Validation
- File Size Validation
- File Type Validation
- Document Storage
- Metadata Generation
- Upload Status Tracking

### API Endpoint

```
POST /documents/upload
```

### Upload Flow

```
Client
   │
   ▼
Upload API
   │
   ▼
Document Validation
   │
   ▼
Document Storage
   │
   ▼
Metadata Generation
   │
   ▼
Upload Complete
```

### Current Capabilities

- Accept PDF architecture documents
- Validate upload requests
- Store uploaded documents
- Generate upload metadata
- Track upload completion status

# Story 2.2 — Document Intelligence Pipeline

**Status:** ✅ Completed

## Objective

Transform uploaded architecture documents into structured intelligence data for future AI processing workflows.

The pipeline extracts document content, preserves structure, and generates metadata required for RAG and AI review capabilities.

---

## Features Implemented

### PDF Processing

- PDF parsing
- Page extraction
- Text extraction

### Document Structure Analysis

- Page metadata extraction
- Heading extraction
- Section detection

### Document Intelligence

- Table extraction
- Document classification
- Structured document output

---

## Document Processing Flow

```text
Uploaded Document
        |
        ▼
PDF Parser
        |
        ▼
Page Extraction
        |
        ▼
Structure Analyzer
        |
        +----------------+
        |                |
        ▼                ▼
 Metadata           Headings
        |
        ▼
 Sections
        |
        ▼
 Tables
        |
        ▼
Document Classification
        |
        ▼
Structured Document
```

---

## Current Capabilities

The Document Intelligence Pipeline can:

- Read uploaded PDF documents
- Extract page-level content
- Identify headings
- Detect document sections
- Extract tables
- Classify document type
- Generate structured document metadata

---

## Technology Components

| Component | Technology |
|---|---|
| PDF Parsing | PyMuPDF |
| Table Extraction | pdfplumber |
| API Layer | FastAPI |
| Processing Layer | Python Services |

---

## Next Story

**Story 2.3 — Text Chunking & Embeddings Pipeline**

Planned:

- Semantic text chunking
- Token management
- Embedding generation
- Vector preparation