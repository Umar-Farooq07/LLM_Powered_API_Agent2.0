from app.services.store_vector import retrieve_context



def get_context(query, document_id,k=3):

    results = retrieve_context(query, document_id, k)

    context_string = ""
    meta_data = []

    for i in results:
        context_string+= i.page_content
        meta_data.append(i.metadata)
    
    return context_string



