# RAG Crash Course with LangChain 🚀

A comprehensive Retrieval-Augmented Generation (RAG) implementation using LangChain, FAISS, and Groq LLM for efficient document question-answering.

## ✨ Features

- **Multi-format Document Support**: PDF, TXT, CSV, Excel, Word, JSON
- **Efficient Vector Search**: FAISS for fast similarity search
- **Fast LLM Integration**: Groq API for high-speed inference
- **Smart Chunking**: Intelligent document splitting with overlap
- **Persistent Storage**: Save and load vector embeddings
- **Customizable RAG**: Configurable chunk size, overlap, and search parameters


⚙️ Configuration
Environment Variables

# Required: Get from https://console.groq.com/
GROQ_API_KEY=your_groq_api_key_here

# Optional: Model configuration
GROQ_MODEL=llama3-8b-8192
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Optional: RAG parameters
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K_RESULTS=5


Available Groq Models
llama3-8b-8192 (Default)

llama3-70b-8192

mixtral-8x7b-32768

gemma-7b-it

Embedding Models
all-MiniLM-L6-v2 (Default, fast and efficient)

all-mpnet-base-v2 (Higher quality, slower)

multi-qa-mpnet-base-dot-v1 (Optimized for Q&A)


Format	Extension	Features
📄 PDF	.pdf	Text extraction, metadata
📝 Text	.txt	Simple text processing
📊 CSV	.csv	Tabular data processing
📈 Excel	.xlsx, .xls	Multiple sheets support
📑 Word	.docx	Document formatting
⚙️ JSON	.json	Structured data parsing


🔧 API Reference
RAGSearch Class
python
class RAGSearch:
    def __init__(self, persist_dir: str = "faiss_store", 
                 embedding_model: str = "all-MiniLM-L6-v2",
                 llm_model: str = None):
        """
        Initialize RAG search system.
        
        Args:
            persist_dir: Directory for vector store persistence
            embedding_model: Sentence transformer model name
            llm_model: Groq model name (default: from env var)
        """
    
    def search_and_summarize(self, query: str, top_k: int = 5) -> str:
        """
        Search documents and generate summary.
        
        Args:
            query: Natural language query
            top_k: Number of top results to consider
            
        Returns:
            Generated summary based on retrieved context
        """
📝 Examples
Example 1: Basic Query
python
rag = RAGSearch()
result = rag.search_and_summarize("What is machine learning?")
print(result)
Example 2: Technical Query
python
query = """
Explain the difference between supervised and unsupervised learning 
with examples from the provided context.
"""
result = rag.search_and_summarize(query, top_k=5)



## DEMO 


