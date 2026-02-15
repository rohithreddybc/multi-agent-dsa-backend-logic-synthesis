from memory.technique_store import technique_store

def get_technique_retriever():
    """Get a retriever for DSA techniques from the vector store."""
    return technique_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,  # Return top 5 most relevant techniques
            "fetch_k": 10,
            "lambda_mult": 0.6  # Diversity vs relevance balance
        }
    )

