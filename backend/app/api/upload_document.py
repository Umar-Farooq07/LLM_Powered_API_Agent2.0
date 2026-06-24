from fastapi import APIRouter, UploadFile, File,HTTPException
from app.services.file_storage import store_document
from app.repositories.document_repositories import store_metadata



router = APIRouter()

@router.post("/upload_document")
async def upload_document(file : UploadFile= File(...)):

    if(file.content_type!= "application/pdf"):
        raise HTTPException(status_code=400, detail="Only upload a pdf file")
    
    content = await file.read()
    storage_info = store_document(file.filename,content)
    store_metadata(storage_info)

    return storage_info
    
    




