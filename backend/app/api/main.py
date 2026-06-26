from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.upload_document import router as upload_document
from app.api.ingestion import router as ingest_document_endpoint
from app.api.query_endpoint import router as query_enpoint


app = FastAPI()
app.include_router(health_router)
app.include_router(upload_document)
app.include_router(ingest_document_endpoint)
app.include_router(query_enpoint)


