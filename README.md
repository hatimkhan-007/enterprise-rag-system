# Enterprise AI Document Analysis System | RAG-Based PDF Q&A

An AI-powered document question-answering application built with **Python, LangChain, OpenAI, Chroma, and Streamlit**. The system enables users to upload PDF documents and ask natural-language questions to retrieve relevant information and generate context-aware answers.

The project demonstrates an end-to-end **Retrieval-Augmented Generation (RAG)** pipeline, combining document processing, vector embeddings, semantic retrieval, and Large Language Models (LLMs) in an interactive web application.

## 🚀 Features

* **PDF Document Ingestion:** Load and extract text from multi-page PDF documents using LangChain's `PyPDFLoader`.
* **Text Chunking:** Split extracted content into manageable, overlapping chunks using `RecursiveCharacterTextSplitter`.
* **Vector Embeddings:** Generate semantic vector representations using OpenAI's `text-embedding-3-small` model.
* **Vector Database:** Store document embeddings and associated text using Chroma.
* **Retrieval-Augmented Generation:** Retrieve relevant document passages and provide them as context to GPT-4o mini.
* **Context-Aware Answers:** Generate responses grounded in retrieved document content, with instructions to acknowledge insufficient information.
* **Interactive Web Interface:** Upload PDFs and ask questions through a Streamlit application.
* **Modular Architecture:** Separate document processing, RAG pipeline construction, and user interface logic into dedicated Python modules.

## 🛠️ Tech Stack

| Technology                      | Purpose                             |
| ------------------------------- | ----------------------------------- |
| Python                          | Application development             |
| LangChain                       | RAG pipeline orchestration          |
| OpenAI GPT-4o mini              | Answer generation                   |
| OpenAI `text-embedding-3-small` | Text embeddings                     |
| Chroma                          | Vector storage and retrieval        |
| PyPDFLoader                     | PDF text extraction                 |
| Streamlit                       | Web interface                       |
| python-dotenv                   | Environment variable management     |
| Git and GitHub                  | Version control and project hosting |

## 🧠 How It Works

```text
PDF Upload
    |
    v
Text Extraction
    |
    v
Text Chunking
    |
    v
Embedding Generation
    |
    v
Chroma Vector Database
    |
    v
User Question
    |
    v
Relevant Chunk Retrieval
    |
    v
LLM + Retrieved Context
    |
    v
Context-Aware Answer
    |
    v
Streamlit Interface
```

The system follows a Retrieval-Augmented Generation workflow:

1. The user uploads a PDF document.
2. The application extracts its text and splits it into overlapping chunks.
3. Each chunk is converted into a vector embedding.
4. Chroma stores the embeddings and their associated document content.
5. When a question is submitted, the retriever identifies relevant chunks.
6. The language model uses the retrieved context to generate an answer.
7. The answer is displayed in the Streamlit interface.

## 📁 Project Structure

```text
project-root/
├── app.py
├── data_processor.py
├── rag_chain.py
├── Documentation.md
├── README.md
├── requirements.txt
├── .env
├── .gitignore
├── temp/
└── chroma_db/
```

**Note:** This is the intended structure. Update it to match the files and directories actually present in your repository. The `.env` file, temporary uploads, and generated vector database files should not be committed unless there is a specific, safe reason to include them.

### Main Components

* `app.py` — Streamlit interface and application workflow.
* `data_processor.py` — PDF loading, text splitting, embedding generation, and vector storage.
* `rag_chain.py` — Language model configuration, prompt template, and RAG chain.
* `Documentation.md` — Detailed project documentation.
* `requirements.txt` — Python dependencies.
* `.gitignore` — Excludes secrets and generated files from version control.

## ⚙️ Installation and Setup

### Prerequisites

* Python 3.10 or a compatible version supported by the dependencies.
* pip package manager.
* An OpenAI API key with access to the required models.
* Git.

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

Replace the placeholders with your actual repository URL and folder name.

### 2. Create a Virtual Environment

```bash
python -m venv ai_project_env
```

Activate it on Windows:

```powershell
.\ai_project_env\Scripts\Activate.ps1
```

For Windows Command Prompt:

```bat
ai_project_env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your_openai_api_key
```

Replace the placeholder with your API key. Never commit actual API credentials to GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## 🔧 Configuration

The initial RAG pipeline uses the following configuration:

| Parameter             | Value                            |
| --------------------- | -------------------------------- |
| Text splitter         | `RecursiveCharacterTextSplitter` |
| Chunk size            | 1,000 characters                 |
| Chunk overlap         | 200 characters                   |
| Embedding model       | `text-embedding-3-small`         |
| Language model        | `gpt-4o-mini`                    |
| Retrieved chunks      | 3                                |
| Vector database       | Chroma                           |
| Persistence directory | `./chroma_db`                    |

These values are initial settings and can be adjusted based on retrieval quality, document characteristics, and API costs.

## 🔐 Security Considerations

* Store API keys in environment variables rather than source code.
* Exclude `.env` from version control.
* Validate uploaded files and enforce appropriate size limits.
* Avoid retaining uploaded documents longer than necessary.
* Add authentication and access controls before supporting sensitive enterprise documents.
* Treat document contents as untrusted input when constructing prompts.

**Important:** These are security recommendations, not a claim that all these protections are already implemented.

## ⚠️ Current Limitations

* The current scope focuses on text extraction from PDF documents.
* Scanned PDFs may require OCR support.
* Answers depend on extraction quality and the relevance of retrieved chunks.
* The application does not guarantee that all generated answers are correct.
* API requests may incur costs.
* Source citations, advanced evaluation, and production access controls may require additional implementation.
* Image understanding and other multimodal capabilities are not included in the initial PDF-based pipeline.

## 🛣️ Future Enhancements

* Support multiple PDF documents in one knowledge base.
* Display source citations and PDF page numbers with answers.
* Add conversational memory and follow-up questions.
* Support DOCX, TXT, and CSV files.
* Add OCR and image-based document understanding.
* Improve retrieval using metadata filtering and reranking.
* Evaluate retrieval quality and answer correctness.
* Add automated tests and robust error handling.
* Deploy the application to a cloud hosting platform.

## 🎯 Learning Outcomes

This project provides practical experience with:

* Generative AI application development.
* Retrieval-Augmented Generation architecture.
* LangChain integrations and prompt engineering.
* Vector embeddings and semantic retrieval.
* Chroma vector database management.
* OpenAI API integration.
* PDF processing and text chunking.
* Streamlit application development.
* Environment configuration and Git-based workflows.

## 📚 Documentation and References

For implementation details, setup instructions, architecture, and future improvements, see [`Documentation.md`](Documentation.md).

* [LangChain Documentation](https://python.langchain.com/docs/introduction/)
* [OpenAI API Documentation](https://platform.openai.com/docs/)
* [Chroma Documentation](https://docs.trychroma.com/)
* [Streamlit Documentation](https://docs.streamlit.io/)

---

**Project Status:** Initial PDF-based RAG application.

**Future Direction:** Evolve the project into a more comprehensive document intelligence system with source citations, multi-document retrieval, multimodal processing, evaluation, and deployment.
