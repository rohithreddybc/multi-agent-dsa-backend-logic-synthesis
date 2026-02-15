from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(
    model_name="./models/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"} 
)

vectorstore = Chroma(
    collection_name="code_memory",
    embedding_function=embedding,
    persist_directory="./memory/chroma"
)
