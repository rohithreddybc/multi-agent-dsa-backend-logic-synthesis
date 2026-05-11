# memory/ret_.py

from memory.vector_store import vectorstore

def get_code_retriever():
    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10,
            "lambda_mult": 0.6
        }
    )
