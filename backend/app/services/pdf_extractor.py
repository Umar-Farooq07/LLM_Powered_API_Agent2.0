import os
from pypdf import PdfReader



def get_text(path):

    if(os.path.exists(path)):
        
        data = PdfReader(path)  
        text =""
        for page in data.pages:
            text+= page.extract_text() or ""
        return text
    
    
    else: 
        return None