# Runbook — Story 2.3 Evidence Management System

## Overview

Story 2.3 implements the Evidence Management System for ArchAI Reviewer.

The purpose of this component is to maintain traceable evidence from architecture documents and provide citations for AI-generated findings.

The evidence layer enables:

- Source traceability
- Evidence retrieval
- Citation generation
- Finding-to-source linking


---

# Architecture Flow


Architecture Document
    |
    v

Document Intelligence Pipeline
    |
    v

Evidence Management System
    |
    v

AI Findings with Citations


---

# Objectives

Implement:

- Evidence domain model
- Evidence schema
- Source reference tracking
- Evidence retrieval
- Citation generation
- Finding linkage foundation


---

# Implementation Structure


backend/app/

├── models
│   └── evidence.py
│
├── schemas
│   └── evidence_schema.py
│
├── services
│   └── evidence_service.py
│
├── api
│   └── evidence.py
│
└── tests
└── test_evidence.py


---

# Evidence Data Model

Evidence stores the relationship between extracted document content and its original source.


Example:

```json
{
    "document_id": "DOC001",
    "page": "12",
    "section": "Database Architecture",
    "content": "Database does not have replication configured"
}

Fields:
Field	Description
document_id	Source document reference
page	Document page number
section	Document section
content	Extracted evidence text


API Endpoints
Create Evidence
Endpoint:
POST /evidence/create

Request:
{
 "document_id":"DOC001",
 "page":"12",
 "section":"Database Architecture",
 "content":"No replication configured"
}

Response:
{
 "id":"E-1",
 "document_id":"DOC001",
 "page":"12",
 "section":"Database Architecture",
 "content":"No replication configured"
}

Retrieve Evidence
Endpoint:
GET /evidence/{document_id}

Example:
GET /evidence/DOC001

Returns all evidence associated with the document.
Citation Generation
Evidence can generate references for AI findings.

Example:
{
 "source":"DOC001",
 "reference":"Page 12, Section Database Architecture",
 "content":"No replication configured"
}

Validation
Run:
python -m backend.app.tests.test_evidence

Expected:
Evidence validation passed ✅