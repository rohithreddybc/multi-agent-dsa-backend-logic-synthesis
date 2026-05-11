from pathlib import Path
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# Absolute path to project root
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "all-MiniLM-L6-v2"
DB_PATH = BASE_DIR / "memory" / "techniques_db"


if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Embedding model not found at {MODEL_PATH}. Please ensure the model is downloaded.")


os.makedirs(DB_PATH, exist_ok=True)


embedding = HuggingFaceEmbeddings(
    model_name=str(MODEL_PATH),
    model_kwargs={"device": "cpu"}
)


technique_store = Chroma(
    collection_name="dsa_techniques",
    embedding_function=embedding,
    persist_directory=str(DB_PATH)
)
