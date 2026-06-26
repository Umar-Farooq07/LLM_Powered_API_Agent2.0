from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import VECTOR_STORAGE_DIR, embedding_model_name



embedding_model = HuggingFaceEmbeddings(
    model_name = embedding_model_name
)

vectorstore = Chroma(
    collection_name="Documents",
    persist_directory= VECTOR_STORAGE_DIR,
    embedding_function= embedding_model
)


def store_in_vdb(chunks, metadata):

        
    vectorstore.add_texts(
        texts=chunks,
        metadatas=metadata
    )

def retrieve_context(query, document_id, k=3):
    results =vectorstore.similarity_search(
        query=query,
        k =k,
        filter={"document_id": document_id}
    )
    return results

