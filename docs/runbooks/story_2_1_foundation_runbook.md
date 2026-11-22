# Story 2.1 — Document Upload System

## Objective

Implement the document upload pipeline for ArchAI Reviewer.

The upload pipeline validates incoming documents, stores them, generates metadata, and prepares them for future document intelligence workflows.

---

# Components

```
backend/app/

├── api/
│   └── documents.py
│
├── services/
│   ├── document_service.py
│   └── metadata_service.py
│
├── storage/
│   └── document_storage.py
│
└── validators/
    └── document_validator.py
```

---

# Upload Workflow

```
Client
   │
   ▼
Upload API
   │
   ▼
Document Validator
   │
   ▼
Document Storage
   │
   ▼
Metadata Service
   │
   ▼
Response
```

---

# Validation Rules

## File Type

Allowed:

```
application/pdf
```

---

## Maximum File Size

```
10 MB
```

---

# Storage Location

```
storage/documents/
```

---

# API

## Upload Document

```
POST /documents/upload
```

Parameters:

| Name | Type | Required |
|------|------|----------|
| project_id | string | Yes |
| file | UploadFile | Yes |

---

# Successful Response

```json
{
  "message": "Document uploaded successfully",
  "document": {
    "filename": "architecture.pdf",
    "storage_path": "storage/documents/architecture.pdf",
    "status": "COMPLETED"
  }
}
```

---

# Validation Commands

## Start Backend

```bash
uvicorn backend.app.main:app --reload
```

---

## Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Run Upload Validation

1. Open Swagger UI.
2. Expand **POST /documents/upload**.
3. Click **Try it out**.
4. Enter a valid `project_id`.
5. Upload a PDF file.
6. Execute the request.

---

# Expected Result

- PDF accepted
- File stored in `storage/documents`
- Metadata generated
- Upload status returned as `COMPLETED`

---

# Completion Criteria

| Item | Status |
|------|--------|
| Upload API implemented | ✅ |
| Storage service implemented | ✅ |
| PDF validation completed | ✅ |
| File size validation completed | ✅ |
| Metadata generation completed | ✅ |
| Upload status tracking completed | ✅ |

---

# Next Story

Story 2.2 — Document Processing Pipeline