from app.services.pdf_extractor import get_text
from app.services.text_chunker import create_chunks
from app.repositories.document_repositories import get_metadata, update_status
from app.services.store_vector import store_in_vdb

import logging
logger = logging.getLogger(__name__)

def ingest_document(document_id):

   logger.info("Getting metadata of %s", document_id)
   metadata = get_metadata(document_id)
   if(metadata==None):
      logger.warning("metadata of %s doesnt exist", document_id)
      return None
   
   text = get_text(metadata["file_path"])
   chunks = create_chunks(text)
   
   chunk_metadata = []
   for i in range(len(chunks)):
      chunk_metadata.append({
         "document_id": document_id,
         "chunk_index" : i

      })


   store_in_vdb(chunks,chunk_metadata)
   update_status(document_id)


