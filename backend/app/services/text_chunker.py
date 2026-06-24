from langchain_text_splitters import RecursiveCharacterTextSplitter



def create_chunks(text):

    if(text=="" or text==None):
        return []
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(text)
    return chunks