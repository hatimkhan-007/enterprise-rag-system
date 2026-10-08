# Enterprise AI Document Analysis System (Multimodal RAG)

An end-to-end, production-grade Generative AI application built with LangChain, OpenAI, and Streamlit. This system allows users to securely upload multi-page enterprise documents (PDFs) and extract targeted semantic insights via a conversational chat interface.

## 🚀 Features
- **Semantic Chunking:** Uses `RecursiveCharacterTextSplitter` to optimize token limits and preserve context.
- **High-Performance Vector Storage:** Leverages a local `Chroma` database for rapid embedding indexing.
- **RAG Architecture:** Plugs an optimized prompt pipeline into `gpt-4o-mini` to eliminate hallucinations.
- **Responsive UI:** Streamlit interface for effortless real-time document ingestion.

## 🛠️ Tech Stack
- **Framework:** LangChain
- **LLM / Embeddings:** OpenAI (GPT-4o mini / text-embedding-3-small)
- **Vector DB:** Chroma
- **Frontend:** Streamlit
- **Language:** Python 3.10+
