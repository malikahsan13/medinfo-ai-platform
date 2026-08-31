MedInfo AI Platform is a production-oriented AI platform designed to assist medical information teams with evidence retrieval, medical inquiry analysis, AI-assisted response generation, citation tracking, and human review.

                 MEDINFO AI PLATFORM

        ┌─────────────────────────────┐
        │   Medical Documents / PDFs  │
        └──────────────┬──────────────┘
                       ↓
              Document Processing
                       ↓
             Chunking + Embeddings
                       ↓
              PostgreSQL + pgvector
                       ↓
      ┌────────────────────────────────┐
      │        Medical Inquiry         │
      └───────────────┬────────────────┘
                      ↓
                Query Analysis
                      ↓
              Hybrid Retrieval
                      ↓
                  Reranking
                      ↓
                RAG Generation
                      ↓
             Citation Generation
                      ↓
           Evidence Verification
                      ↓
          Hallucination Detection
                      ↓
              Human Reviewer
                 ↙       ↘
            APPROVE      REJECT
                ↓
          Final Response

tech stack

Backend

Python
FastAPI
SQLAlchemy
PostgreSQL
Alembic

AI

OpenAI API
LangChain
LangGraph
RAG
Embeddings
Hybrid Search
Reranking
Structured LLM outputs
AI evaluation

Infrastructure

Redis
Celery
Docker
AWS S3
AWS deployment
GitHub Actions CI/CD

Vector search

PostgreSQL + pgvector initially
