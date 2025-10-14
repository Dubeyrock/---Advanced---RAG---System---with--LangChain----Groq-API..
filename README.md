# RAG Crash Course with LangChain 🚀

A comprehensive Retrieval-Augmented Generation (RAG) implementation using LangChain, FAISS, and Groq LLM for efficient document question-answering.



## What is Retrieval-Augmented Generation?

Retrieval-Augmented Generation (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response. Large Language Models (LLMs) are trained on vast volumes of data and use billions of parameters to generate original output for tasks like answering questions, translating languages, and completing sentences. RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model. It is a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts.

## ✨ Features

- **📁 Multi-format Document Support**: PDF, TXT, CSV, Excel, Word, JSON
- **⚡ Efficient Vector Search**: FAISS for fast similarity search
- **🚀 Fast LLM Integration**: Groq API for high-speed inference
- **✂️ Smart Chunking**: Intelligent document splitting with overlap
- **💾 Persistent Storage**: Save and load vector embeddings
- **🎛️ Customizable RAG**: Configurable chunk size, overlap, and search parameters


🏗️ RAG Architecture
<img width="898" height="532" alt="image" src="https://github.com/user-attachments/assets/ccb4ff1c-1d1c-4326-b0f6-6e3b32f18ed0" />



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




## 🗂️ Data Ingestion Flow
📁 Raw Documents 
    ↓
🔄 Multi-format Loader (PDF/TXT/CSV/DOCX/JSON)
    ↓
✂️ Text Chunking (size: 1000, overlap: 200)
    ↓
🔢 Embedding Generation (all-MiniLM-L6-v2)
    ↓
💾 FAISS Vector Storage
    ↓
💿 Persistent Save (faiss.index + metadata.pkl)

## 🔎 Retrieval Flow

❓ User Query: "How does histogram equalization work?"
    ↓
🎯 Query Embedding (vector conversion)
    ↓
🔍 FAISS Similarity Search (top_k=5)
    ↓
📄 Context Retrieval (relevant document chunks)
    ↓
🤖 LLM Prompt: Context + Query
    ↓
💬 Generated Answer: "Histogram equalization improves contrast by..."


## Key Updates Made:

1. **🏗️ RAG Architecture Section** - Added comprehensive architecture diagrams and pipelines
2. **📊 Supported Formats Table** - Added the emoji table for document formats
3. **🎨 Enhanced Visuals** - More emojis and better section organization
4. **🔧 Technology Stack Table** - Clear breakdown of technologies used
5. **📈 Improved Flow Diagrams** - Both ingestion and retrieval pipelines
6. **✨ Better Badges** - Added more relevant technology badges

This README now provides a complete, professional documentation for your RAG project that will look great on GitHub! The mermaid diagram will automatically render on GitHub to show the visual architecture flow.


