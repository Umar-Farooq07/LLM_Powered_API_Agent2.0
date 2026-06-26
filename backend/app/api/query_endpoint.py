from fastapi import APIRouter, HTTPException

from app.schemas.query import QueryRequest
from app.schemas.query_response import QueryResponse
from app.services.query_service import get_context
from app.services.llm_service import generate_answer
from app.repositories.document_repositories import get_metadata
from app.core.config import top_context_answer

router = APIRouter(prefix="/documents", tags=["Query"])


@router.post("/{document_id}/query", response_model=QueryResponse)
def query_document(document_id: str, request: QueryRequest):

    # Check whether document exists
    metadata = get_metadata(document_id)

    if metadata is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    # Check whether document has been indexed
    if metadata["status"] != "indexed":
        raise HTTPException(
            status_code=400,
            detail="Document has not been indexed yet."
        )

    # Retrieve relevant context
    context = get_context(
        query=request.query,
        document_id=document_id,
        k=top_context_answer,
    )

    if not context:
        raise HTTPException(
            status_code=404,
            detail="No relevant context found."
        )

    # Generate answer
    answer = generate_answer(
        question=request.query,
        context=context,
    )

    return QueryResponse(
        document_id=document_id,
        query=request.query,
        answer=answer,
    )