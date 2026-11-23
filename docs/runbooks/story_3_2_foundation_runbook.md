Content:
# Runbook — Story 3.2 Implement Hybrid Retrieval

## Overview

Story 3.2 implements the retrieval intelligence layer of the ArchAI Reviewer Enterprise RAG Pipeline.

The objective is to improve knowledge retrieval accuracy by combining:

- Semantic vector search
- Keyword-based retrieval
- Result fusion
- Ranking algorithm


---

# Story Objective

Build a hybrid retrieval engine capable of:

- Finding semantically similar architecture knowledge
- Finding exact keyword matches
- Combining multiple retrieval strategies
- Ranking the most relevant chunks
- Returning high-quality context for LLM analysis


---

# Architecture Flow

                User Query
                     |
                     v
          Hybrid Retrieval Service
                     |
    +----------------+----------------+
    |                                 |
    v                                 v
 Vector Similarity Search          BM25 Keyword Search
    |                                 |
    |                                 |
    +----------------+----------------+
                     |
                     v
              Result Fusion
                     |
                     v
             Ranking Algorithm
                     |
                     v
          Top-K Relevant Chunks
                     |
                     v
             RAG Context Layer



---

# Implementation Components


## Project Structure


backend/app/

├── api
│   └── retrieval.py
│
├── models
│   └── retrieval_result.py
│
├── schemas
│   └── retrieval_schema.py
│
├── services
│   ├── vector_search_service.py
│   ├── keyword_search_service.py
│   ├── result_fusion_service.py
│   ├── ranking_service.py
│   └── hybrid_retrieval_service.py
│
└── tests
├── test_vector_search.py
├── test_keyword_search.py
├── test_result_fusion.py
└── test_hybrid_retrieval.py

---

# Completed Tasks


# 1. Vector Similarity Search

## Purpose

Retrieve chunks based on semantic meaning using embeddings.


Flow:

Query
 |
Embedding Generation
 |
Query Vector
 |
Vector Store Search
 |
Similarity Score
 |
Top Results


Implementation:

VectorSearchService
Capabilities:

- Generate query embedding
- Compare with stored vectors
- Calculate cosine similarity
- Return top-k chunks


Validation:
Vector search validation passed ✅


---

# 2. BM25 Keyword Search

## Purpose
Retrieve chunks based on exact keyword relevance.


Technology:
BM25 (Best Matching 25)


Implementation:
KeywordSearchService


Capabilities:
- Build keyword index
- Tokenize documents
- Match query keywords
- Generate keyword score


Validation:
Keyword search validation passed ✅


---

# 3. Result Fusion


## Purpose

Combine semantic and keyword results.

Implementation:
ResultFusionService

Fusion Process:

Vector Results
   +
Keyword Results
   |
   v
Combined Results


Example:
```json
{
 "chunk_id":"CH001",
 "vector_score":0.90,
 "keyword_score":0.80
}

Validation:
Result fusion validation passed ✅

4. Ranking Algorithm
Purpose
Rank final retrieval results.

Implementation:
RankingService

Scoring Formula:

Final Score =
(Vector Score × 0.5)
+
(BM25 Score × 0.3)
+
(Metadata Score × 0.2)

Ranking Factors:
Factor	Weight
Semantic similarity	50%
Keyword relevance	30%
Metadata relevance	20%


Output:
{
 "chunk_id":"CH001",
 "final_score":0.89
}

5. Hybrid Retrieval API
Endpoint:
POST /retrieval/search

Request:
{
 "query":"database scalability architecture",
 "top_k":5
}

Response:
[
 {
  "chunk_id":"CH001",
  "document_id":"DOC001",
  "content":"Database replication strategy",
  "final_score":0.89
 }
]

Validation Procedures
Vector Search
Command:
python -m backend.app.tests.test_vector_search

Expected:
Vector search validation passed ✅

Keyword Search
Command:
python -m backend.app.tests.test_keyword_search

Expected:
Keyword search validation passed ✅

Result Fusion
Command:
python -m backend.app.tests.test_result_fusion

Expected:
Result fusion validation passed ✅

Hybrid Retrieval
Command:
python -m backend.app.tests.test_hybrid_retrieval

Expected:
Hybrid retrieval validation passed ✅

Story Completion Checklist
Component	Status
Vector similarity search	✅
BM25 keyword retrieval	✅
Result fusion	✅
Ranking algorithm	✅
Hybrid retrieval service	✅
Retrieval API	✅
Validation tests	✅


Story Status
Completed ✅

Next Story
Story 3.3 — Implement Reranking