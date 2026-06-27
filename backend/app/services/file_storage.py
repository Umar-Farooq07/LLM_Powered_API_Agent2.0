import os
import uuid
from app.core.config import DOCUMENTS_STORAGE_DIR

import logging
logger= logging.getLogger(__name__)

def store_document(file_name , content):

    doc_id = str(uuid.uuid4())
    folder_path = os.path.join(DOCUMENTS_STORAGE_DIR,doc_id)
    logger.info("Storing the file : %s", file_name)
    os.makedirs(folder_path,exist_ok=True)
    file_path = os.path.join(folder_path, "original.pdf")

    with open(file_path, "wb") as f:
        f.write(content)
    logger.info("Stored the file : %s", file_name)
    return {
        "document_id" : doc_id,
        "file_name"   : file_name,
        "stored_path" : file_path,
        "status"      : "uploaded"
    }
    

