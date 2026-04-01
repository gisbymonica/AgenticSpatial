# models/embeddings.py

from sentence_transformers import SentenceTransformer


class GeoEmbeddingModel:
    """
    Wrapper for sentence-transformer embeddings 
    used in ChromaDB / Pinecone RAG pipelines.
    """

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        """
        Computes dense vector embeddings for list of strings.
        """
        return self.model.encode(texts, convert_to_numpy=True)

    def embed_one(self, text: str):
        return self.embed([text])[0]