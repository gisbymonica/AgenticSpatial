# agents/rag_agent.py

import chromadb
from chromadb.utils import embedding_functions
import json
import os
from models.embeddings import GeoEmbeddingModel
from config import CHROMA_DB_PATH


def init_rag_collection():
    """
    Initialize or load the ChromaDB collection for metadata.
    """
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    return client.get_or_create_collection(
        name="geo_metadata",
        embedding_function=embed_fn
    )


def ingest_metadata(metadata_folder="data/metadata/"):
    """
    Loads all metadata JSON files into ChromaDB for RAG.
    """
    collection = init_rag_collection()
    embed_model = GeoEmbeddingModel()

    files = [f for f in os.listdir(metadata_folder) if f.endswith(".json")]

    for f in files:
        path = os.path.join(metadata_folder, f)
        with open(path, "r") as fp:
            content = json.load(fp)

        doc_id = content.get("id", f)
        text = json.dumps(content, indent=2)

        emb = embed_model.embed_one(text)

        collection.add(
            documents=[text],
            embeddings=[emb.tolist()],
            ids=[doc_id]
        )

    print(f"[RAG] Ingested {len(files)} metadata documents.")


def retrieve_relevant_metadata(query, n=5):
    """
    Query ChromaDB to retrieve metadata relevant to the user query.
    """
    collection = init_rag_collection()
    result = collection.query(query_texts=[query], n_results=n)
    return result