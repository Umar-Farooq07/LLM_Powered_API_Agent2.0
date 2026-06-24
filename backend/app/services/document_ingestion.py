from app.services.pdf_extractor import get_text
from app.services.text_chunker import create_chunks
from app.repositories.document_repositories import get_metadata


def ingest_document(document_id):
    metadata = get_metadata(document_id)
    if(metadata==None):
       return None
    text = get_text(metadata["file_path"])
    chunks = create_chunks(text)
    
    return chunks