import json
import os

from app.core.config import DOCUMENTS_STORAGE_DIR



def store_metadata(metadata : dict):

    file_path= os.path.join(DOCUMENTS_STORAGE_DIR , "metadata.json")
    if(os.path.exists(file_path)):
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = {}
    
    data[metadata["document_id"]] = {
        "file_path" : metadata["stored_path"],
        "file_name" : metadata["file_name"],
        "status"    : metadata["status"]
    }

    with open(file_path, 'w') as f:
        json.dump(data,f,indent=4)


        

def get_metadata(document_id):

    file_path = os.path.join(DOCUMENTS_STORAGE_DIR, "metadata.json")
    if(os.path.exists(file_path)):
        with open(file_path, 'r') as f:
            data = json.load(f)
    else:
        return None
    
    if document_id in data.keys():
        return data[document_id]
    else:
        return None


def update_status(document_id):

    file_path = os.path.join(DOCUMENTS_STORAGE_DIR, "metadata.json")
    with open(file_path, "r") as f:
        data = json.load(f)

    doc_metadata = data[document_id]
    doc_metadata["status"] = "indexed"

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    

    
    

