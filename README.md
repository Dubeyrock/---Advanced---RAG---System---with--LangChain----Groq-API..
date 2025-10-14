# RAG Crash Course with LangChain 🚀

A comprehensive Retrieval-Augmented Generation (RAG) implementation using LangChain, FAISS, and Groq LLM for efficient document question-answering.


🏗️ RAG Architecture
![WhatsApp Image 2025-10-13 at 18 52 00_8b436af8](https://github.com/user-attachments/assets/8cc9b063-cba4-4e83-b195-e8fa06706411)
![WhatsApp Image 2025-10-13 at 17 16 54_213f00e0](https://github.com/user-attachments/assets/dab092d3-fc7d-4dd5-9628-65accaae84bc)
<img width="1724" height="2550" alt="r1" src="https://github.com/user-attachments/assets/c4a82c1b-cb61-4b56-aace-da1fb3d3a93d" />




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


## 📊 Supported Document Formats

| Format | Extension | Features |
|--------|-----------|----------|
| 📄 PDF | `.pdf` | Text extraction, metadata |
| 📝 Text | `.txt` | Simple text processing |
| 📊 CSV | `.csv` | Tabular data processing |
| 📈 Excel | `.xlsx`, `.xls` | Multiple sheets support |
| 📑 Word | `.docx` | Document formatting |
| ⚙️ JSON | `.json` | Structured data parsing |

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

 """

## DEMO 
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7b8be4c7-fd2c-4648-b35d-f68bbca98f08" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/85fef60d-1e50-4e7e-bc38-e9f74b4e7391" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/02e2607e-1774-4378-ac1f-af9a0f52dcfc" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e6a8dc69-cd8d-47bf-8e8d-d0f19445e7ae" />

<img width="1920" height="1080" alt="Screenshot (3413) - Copy" src="https://github.com/user-attachments/assets/db2814c5-f3f9-4370-ab52-89f860320687" />

<img width="1920" height="1080" alt="Screenshot (3414)" src="https://github.com/user-attachments/assets/db5dd9ee-7bb5-4832-b3f9-d4bc99b1f416" />





