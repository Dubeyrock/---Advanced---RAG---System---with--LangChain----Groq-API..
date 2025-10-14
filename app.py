from src.data_loader import load_all_documents
#from src.embedding import EmbeddingPipeline
from src.vector_store import FaissVectorStore
from src.search import RAGSearch
## examples usage

if __name__ == "__main__":
    docs=load_all_documents("data")
    store=FaissVectorStore("faiss_store")
    #store.build_from_documents(docs)
    store.load()
    #EmbeddingPipeline().embed_chunks(docs)
    #chunks = EmbeddingPipeline().chunk_documents(docs)
    #chunkvector = EmbeddingPipeline().embed_chunks(chunks)

    rag_search = RAGSearch()
    query = "How does histogram equalization improve image contrast?"
    summary = rag_search.search_and_summarize(query,top_k=3)
    print("summary:",summary)
   
