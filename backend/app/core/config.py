from dotenv import load_dotenv
import os

load_dotenv()

DOCUMENTS_STORAGE_DIR = "storage/documents"
VECTOR_STORAGE_DIR = "VectorStore"
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

embedding_model_name ="BAAI/bge-small-en-v1.5"


config_repo_id = "Qwen/Qwen2.5-7B-Instruct"
config_temperatures = 0.2
config_max_new_tokens= 1024
config_chunk_size = 1000
config_chunk_overlap = 100


top_context_answer = 3
