# Story 1.3 — Define Core Data Models Runbook

## Objective

Create the domain data contracts required by ArchAI Reviewer.

These models support future:

- Document processing
- RAG pipeline
- LangGraph agents
- AI evaluation
- Human approval workflow

---

# Implementation Location

```
backend/app/

├── models
│
├── schemas
│
└── tests
```

---

# Domain Models

## Project

Purpose:

Represents an architecture review project.

Fields:

- id
- name
- description
- owner_id
- created_at
- updated_at


---

## Document

Purpose:

Represents uploaded architecture artifacts.

Fields:

- id
- project_id
- filename
- document_type
- storage_path
- uploaded_by
- uploaded_at


---

## Review

Purpose:

Tracks architecture review execution.

Fields:

- id
- project_id
- document_id
- status
- reviewer
- started_at
- completed_at


---

## Finding

Purpose:

Stores AI-generated architecture findings.

Fields:

- id
- review_id
- category
- title
- description
- severity
- confidence_score
- recommendation
- evidence_reference


---

## Evaluation

Purpose:

Stores AI quality evaluation results.

Fields:

- id
- review_id
- metric_name
- metric_score
- evaluator_type

---

# API Schemas

Created:

```
ProjectCreateSchema
ProjectResponseSchema

DocumentUploadSchema
DocumentResponseSchema

ReviewCreateSchema
ReviewResponseSchema

FindingResponseSchema

EvaluationResponseSchema
```

---

# Validation Commands

## Model Validation

Run:

```bash
python -m backend.app.tests.test_models
```

Expected:

```
All domain model validations passed ✅
```

---

## Schema Validation

Run:

```bash
python -m backend.app.tests.test_schemas
```

Expected:

```
All schema validations passed ✅
```

---

## Import Validation

Run:

```bash
python -m backend.app.tests.test_imports
```

Expected:

```
Models imported successfully ✅
Schemas imported successfully ✅
```

---

## Validate AI Platform Configuration

Run:

```bash
python -m ai_engine.validation.ai_platform_check
```

Expected:

```text
============================================================
ArchAI Reviewer - AI Platform Validation
============================================================

✓ Configuration loaded

✓ LLM connection successful

✓ Embedding generation successful

✓ LangSmith tracing enabled


AI Platform Ready ✅
```

---

# Completion Criteria

| Item | Status |
|---|---|
| Domain models created | ✅ |
| API schemas created | ✅ |
| Validation completed | ✅ |
| Import checks passed | ✅ |

---

# Result

Story 1.3 establishes the data contract foundation for future ArchAI Reviewer capabilities.

Next:

Story 2.1 — Document Upload System