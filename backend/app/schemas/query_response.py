from pydantic import BaseModel


class QueryResponse(BaseModel):
    document_id: str
    query: str
    answer: str