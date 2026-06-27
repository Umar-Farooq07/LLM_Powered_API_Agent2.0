from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.config import config_chunk_size,config_chunk_overlap

import logging
logger = logging.getLogger(__name__)



def create_chunks(text):

    if(text=="" or text==None):
        logger.warning("No text exists")
        return []
    
    logger.info("Chunking the text")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config_chunk_size,
        chunk_overlap=config_chunk_overlap
    )
    logger.info("Text chunking completed")
    chunks = splitter.split_text(text)
    return chunks