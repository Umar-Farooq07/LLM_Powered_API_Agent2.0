from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.config import config_chunk_size,config_chunk_overlap



def create_chunks(text):

    if(text=="" or text==None):
        return []
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config_chunk_size,
        chunk_overlap=config_chunk_overlap
    )
    chunks = splitter.split_text(text)
    return chunks