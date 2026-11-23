Content:
# Runbook — Story 3.1 Build Embedding Pipeline

## Overview

Story 3.1 implements the embedding foundation for the ArchAI Reviewer Enterprise RAG Pipeline.

The objective is to transform document chunks into vector representations, store them with metadata, and prepare the knowledge base for semantic retrieval.

---

# Story Objective

Build an embedding pipeline capable of:

- Generating embeddings from text chunks
- Storing vectors
- Maintaining chunk metadata
- Creating an indexing foundation
- Preparing data for retrieval workflows

---

# Architecture Flow

Architecture Document
    |
    v
Document Intelligence Layer
    |
    v
Evidence Management Layer
    |
    v
Text Chunk Processing
    |
    v
Embedding Generation
    |
    v
Vector Index
    |
    v
Retrieval Pipeline

---

# Implementation Components

## Project Structure

backend/app/

├── api
│   ├── chunks.py
│   └── embeddings.py
│
├── models
│   ├── document_chunk.py
│   └── embedded_chunk.py
│
├── processors
│   └── text_chunk_processor.py
│
├── schemas
│   └── embedding_schema.py
│
├── services
│   ├── chunk_service.py
│   ├── embedding_service.py
│   ├── embedding_pipeline_service.py
│   └── vector_index_service.py
│
├── vectorstore
│   └── vector_store.py
│
└── tests
├── test_chunking.py
├── test_embeddings.py
└── test_vectorstore.py

---

# Tasks Completed

## 1. Configure Embedding Model

Technology:
Ollama Embeddings
Model:nomic-embed-text

Validation:
```powershell
ollama list

Expected:
nomic-embed-text:latest

2. Text Chunk Processing
Purpose:

Convert extracted document content into smaller searchable units.

Example:

Input:
Database architecture uses a single database instance.

Output:
{
 "chunk_id":"CH001",
 "document_id":"DOC001",
 "content":"Database architecture uses a single database instance.",
 "token_count":8
}

3. Embedding Generation
Service
EmbeddingService

Responsibility:
- Receive text chunks
- Generate vector embeddings
- Return numerical representations
Example:

Input:
{
 "content":"Database architecture"
}

Output:
{
 "embedding":[
    0.012,
    -0.045,
    0.067
 ]
}

4. Vector Storage
Component
VectorStore

Purpose:

Store generated embeddings with metadata.

Stored information:
{
 "chunk_id":"CH001",
 "document_id":"DOC001",
 "embedding":[
 ],
 "metadata":{
     "token_count":50
 }
}

5. Indexing Pipeline
Component
VectorIndexService

Responsibilities:
- Receive embedded chunks
- Attach metadata
- Store vectors
- Maintain searchable index

Pipeline:
Chunk
 |
Embedding Generation
 |
Embedded Chunk
 |
Vector Index
 |
Stored Vector

API Endpoints
Generate Embeddings
Endpoint:
POST /embeddings/generate

Request:
[
 {
  "chunk_id":"CH001",
  "document_id":"DOC001",
  "content":"Database does not have replication configured",
  "token_count":8
 }
]

Response:
[
 {
  "chunk_id":"CH001",
  "document_id":"DOC001",
  "content":"Database does not have replication configured",
  "token_count":8,
  "embedding":[
      0.012,
      0.034
  ]
 }
]

Validation Procedures
1. Validate Embedding Generation
Run:
python -m backend.app.tests.test_embeddings

Expected:
Embedding generation validation passed ✅

2. Validate Vector Storage
Run:
python -m backend.app.tests.test_vectorstore

Expected:
Vector storage validation passed ✅

Completion Checklist
Item	Status
Embedding model configured	✅
Chunk embedding generation	✅
Ollama embedding integration	✅
Chunk metadata handling	✅
Vector storage implementation	✅
Indexing pipeline foundation	✅
Embedding validation	✅
Vector storage validation	✅


Story Status: Completed ✅

Next Story
Story 3.2 — Implement Hybrid Retrieval

Objective:
Build retrieval intelligence using:
- Vector similarity search
- Keyword search (BM25)
- Result fusion
- Ranking algorithm

After adding this file:

```powershell
git add docs/runbooks/story_3_1_embedding_pipeline_runbook.md

git commit -m "Add Story 3.1 embedding pipeline runbook"

Story 3.1 is now properly documented and ready for the transition to Story 3.2 — Hybrid Retrieval.