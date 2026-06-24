from fastapi import APIRouter
from app.services.document_ingestion import ingest_document


router = APIRouter()

@router.get("/documents/{document_id}")
def ingest_document_endpoint(document_id: str):
    chunks = ingest_document(document_id)
    return chunks