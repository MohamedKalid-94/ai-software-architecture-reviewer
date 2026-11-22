## Filename

```text
docs/runbooks/story_1_2_genai_platform_runbook.md

Purpose:
Documents:
- Ollama setup
- LLM validation
- Embedding validation
- LangSmith validation

Content:
# Story 1.2 - Configure GenAI Platform


## Objective
Configure:
- LangChain
- Ollama LLM
- Embeddings
- LangSmith
- AI validation

---

# AI Runtime

Provider:Ollama
LLM:qwen2.5:3b
Embedding:nomic-embed-text

---

# Verify Ollama

Run:

```bash
ollama list

Expected:
qwen2.5:3b
nomic-embed-text

Run AI Platform Validation
From project root:
python -m ai_engine.validation.ai_platform_check

Expected:
ArchAI Reviewer - AI Platform Validation


✓ Configuration loaded
✓ LLM connection successful
✓ Embedding generation successful
✓ LangSmith tracing enabled

AI Platform Ready: Test Individual Components
Test LLM
python -m ai_engine.validation.test_llm

Expected:
AI response displayed

Test Embeddings
python -m ai_engine.validation.test_embeddings

Expected:
Embedding dimension: 768

Troubleshooting
LLM Error
Check:
ollama list

Start Ollama:
ollama serve

LangSmith Not Showing Traces
Check:
.env
LANGSMITH_API_KEY=
LANGSMITH_TRACING=true

---