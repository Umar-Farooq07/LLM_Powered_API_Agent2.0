import os
from pypdf import PdfReader

import logging

logger = logging.getLogger(__name__)



def get_text(path):

    if(os.path.exists(path)):

        logger.info("Extracting pdf from path %s ", path)
        data = PdfReader(path)  
        text =""
        for page in data.pages:
            text+= page.extract_text() or ""
        
        logger.info("Extracted pdf from path %s ", path)
        return text
    
    
    else: 
        logger.warning("Pdf path doesn't exist")
        return None