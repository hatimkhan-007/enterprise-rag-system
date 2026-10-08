# Enterprise AI Document Intelligence — RAG-Based Document Q&A System

## 1. Project Overview

The **Enterprise AI Document Intelligence System** is an AI-powered document question-answering application that allows users to upload PDF documents and ask questions about their contents using natural language.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded documents and provide contextual answers using a Large Language Model (LLM).

Instead of relying entirely on the model's pre-trained knowledge, the application retrieves relevant document passages and supplies them to the model as context before generating an answer.

The application combines document processing, text embeddings, semantic search, vector storage, and a web-based interface to create a practical Generative AI solution.

### Key Objectives

* Build an end-to-end Generative AI application.
* Implement a document ingestion and text-processing pipeline.
* Convert document chunks into vector embeddings.
* Store and retrieve document information using a vector database.
* Generate context-aware answers using a Large Language Model.
* Provide an interactive interface for uploading documents and asking questions.
* Develop practical skills in AI application development and backend integration.

## 2. Problem Statement

Organizations and individuals frequently work with lengthy documents such as reports, research papers, technical manuals, policies, and business documentation.

Manually searching through these documents can be time-consuming. General-purpose AI assistants may also provide inaccurate answers when they lack access to the specific document being analyzed.

This project addresses these challenges by allowing users to ask questions directly about an uploaded PDF and receive answers based on relevant document content.

## 3. Proposed Solution

The application follows a Retrieval-Augmented Generation workflow.

1. The user uploads a PDF document through the web interface.
2. The application extracts text and document metadata.
3. The extracted text is divided into smaller, overlapping chunks.
4. An embedding model converts each chunk into a numerical vector representation.
5. The vectors and their associated text are stored in a Chroma vector database.
6. When the user asks a question, the system retrieves the most relevant document chunks.
7. The retrieved information is passed to the language model as contextual information.
8. The model generates an answer based on the retrieved content.
9. The answer is displayed in the Streamlit interface.

The goal is to make document analysis faster, more interactive, and easier to use.

## 4. Technology Stack

| Technology                     | Purpose                                                                 |
| ------------------------------ | ----------------------------------------------------------------------- |
| Python                         | Core programming language                                               |
| LangChain                      | Connecting document processing, retrieval, prompts, and language models |
| OpenAI API                     | Providing embedding and language-model capabilities                     |
| `text-embedding-3-small`       | Generating vector embeddings                                            |
| GPT-4o mini                    | Generating contextual answers                                           |
| Chroma                         | Storing and retrieving vector embeddings                                |
| PyPDFLoader                    | Loading and extracting text from PDF documents                          |
| RecursiveCharacterTextSplitter | Splitting text into manageable chunks                                   |
| Streamlit                      | Building the interactive web interface                                  |
| python-dotenv                  | Loading configuration values from environment variables                 |
| Git and GitHub                 | Version control and project hosting                                     |

## 5. System Architecture

The application consists of four major components.

### 5.1 Document Processing Module

This component loads the uploaded PDF, extracts its text, and divides it into smaller chunks.

The text splitter uses configurable chunk sizes and overlapping text segments to preserve context across chunk boundaries.

### 5.2 Embedding and Vector Storage Module

The embedding model transforms document chunks into numerical vector representations.

Chroma stores the vectors alongside their associated text and metadata. These vectors support semantic retrieval, allowing the system to identify passages relevant to a user's question.

### 5.3 Retrieval-Augmented Generation Module

The RAG pipeline connects the retriever to the language model.

When a question is submitted, the retriever selects relevant chunks from the document. The language model receives those chunks as context and generates a response.

The prompt instructs the model to acknowledge when the provided context does not contain enough information to answer a question.

### 5.4 User Interface Module

The Streamlit interface allows users to upload PDF files, enter questions, and view generated answers.

It provides a simple interface for interacting with the underlying document-processing and question-answering pipeline.

### Architecture Diagram

```text
              User
               |
               v
       Streamlit Interface
               |
               v
         Upload PDF File
               |
               v
       PDF Text Extraction
               |
               v
       Text Chunking
               |
               v
       Embedding Generation
               |
               v
        Chroma Vector DB
               |
               v
       User Submits Question
               |
               v
       Semantic Retrieval
               |
               v
       Relevant Text Chunks
               |
               v
       LLM + Context Prompt
               |
               v
        Generated Answer
               |
               v
       Display in Streamlit
```

## 6. Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation is an approach that combines information retrieval with language generation.

A conventional language model generates answers using its learned parameters and the information supplied in the prompt. A RAG system first searches an external knowledge source and then uses the retrieved information to help generate an answer.

In this project, the uploaded PDF serves as the knowledge source.

### Main RAG Components

**Document ingestion:** Extracts content from the source document.

**Text chunking:** Divides the document into smaller sections.

**Embeddings:** Represent the meaning of text as numerical vectors.

**Vector database:** Stores embeddings and associated document content.

**Retriever:** Finds relevant document chunks for a question.

**Language model:** Uses the retrieved context to generate a natural-language response.

RAG can improve answer relevance and help ground responses in document content. However, it does not guarantee that every answer will be correct, so generated answers should be checked against the original document when accuracy is important.

## 7. Document Processing Strategy

The application uses the `RecursiveCharacterTextSplitter` from LangChain.

The initial configuration is:

* **Chunk size:** 1,000 characters
* **Chunk overlap:** 200 characters
* **Number of retrieved chunks:** 3

### Why Chunking Is Necessary

Large documents may exceed the amount of text that can be conveniently supplied to a language model in a single request.

Chunking divides the document into smaller sections that can be embedded, indexed, and retrieved independently.

### Why Overlap Is Used

Some important information may span the boundary between two chunks. Overlapping sections help preserve context that might otherwise be lost.

### Why Retrieve Three Chunks?

The initial retriever configuration selects the three most relevant chunks for a question. This is a starting configuration rather than a universally optimal value; retrieval quality can be evaluated and adjusted as the project develops.

## 8. Vector Embeddings and Chroma

### Vector Embeddings

Embeddings are numerical representations of text. Text with similar meanings can have nearby representations in embedding space.

The project uses OpenAI's `text-embedding-3-small` model to create embeddings for document chunks and user questions.

### Chroma Vector Database

Chroma stores the embeddings and associated document information so that relevant chunks can be retrieved when a user asks a question.

The initial implementation configures a local persistence directory:

```text
./chroma_db
```

This directory is intended to retain vector database data locally between application runs. The implementation should be tested to ensure that repeated uploads and indexing operations behave as expected.

## 9. Language Model and Prompt Engineering

The application uses GPT-4o mini through LangChain's `ChatOpenAI` integration.

The model is configured with a temperature of `0`, which favors more consistent responses rather than deliberately varied outputs.

The system prompt instructs the model to:

* Answer questions using the supplied document context.
* Avoid intentionally introducing unsupported information.
* Acknowledge when the retrieved context does not provide an answer.

Prompt instructions alone cannot eliminate hallucinations. Retrieval quality, document extraction, and answer verification also influence the system's reliability.

## 10. User Interface

The application uses Streamlit to provide a browser-based interface.

### Current Interface Features

* PDF file upload.
* Upload status feedback.
* Document processing feedback.
* A natural-language question input.
* Retrieval and answer generation.
* Display of the generated answer.

The interface is intended to make the application accessible to users who do not need to interact directly with Python scripts or API calls.

## 11. Project Structure

The repository is organized around separate modules for document processing, RAG orchestration, and the web interface.

```text
project-root/
│
├── app.py
├── data_processor.py
├── rag_chain.py
├── Documentation.md
├── requirements.txt
├── .env
├── .gitignore
│
├── temp/
│   └── Uploaded PDF files
│
└── chroma_db/
    └── Local vector database data
```

**Note:** The directory tree represents the intended organization. The actual repository may differ depending on the files created during implementation.

### File Descriptions

| File or Directory   | Responsibility                                                   |
| ------------------- | ---------------------------------------------------------------- |
| `app.py`            | Streamlit interface and application workflow                     |
| `data_processor.py` | PDF loading, chunking, embedding, and vector storage             |
| `rag_chain.py`      | Language model configuration, prompt construction, and RAG chain |
| `Documentation.md`  | Project documentation                                            |
| `requirements.txt`  | Python dependency declarations                                   |
| `.env`              | Local environment variables and API credentials                  |
| `.gitignore`        | Excludes sensitive files, generated data, and temporary files    |
| `temp/`             | Temporary storage for uploaded PDFs                              |
| `chroma_db/`        | Local vector database storage                                    |

## 12. Installation and Setup

### Prerequisites

Before running the application, ensure that the following are available:

* Python 3.10 or a compatible Python version supported by the selected dependencies.
* pip package manager.
* An OpenAI API key with access to the required models.
* Git, if cloning the repository.

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

Replace the placeholders with the actual repository URL and directory name.

### Step 2: Create a Virtual Environment

```bash
python -m venv ai_project_env
```

### Step 3: Activate the Virtual Environment

For Windows Command Prompt:

```bat
ai_project_env\Scripts\activate
```

For Windows PowerShell:

```powershell
.\ai_project_env\Scripts\Activate.ps1
```

For macOS or Linux:

```bash
source ai_project_env/bin/activate
```

### Step 4: Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages required by the implementation and resolve any version compatibility issues before running the application.

### Step 5: Configure the API Key

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your_openai_api_key
```

Replace the placeholder with your own API key.

**Security:** Never commit a real API key to GitHub. Ensure `.env` is listed in `.gitignore`. If a key is accidentally published, revoke it and generate a replacement.

### Step 6: Run the Application

```bash
streamlit run app.py
```

Streamlit will start a local development server and display the local URL in the terminal.

Open that URL in a browser to use the application.

## 13. How to Use the Application

1. Start the application using Streamlit.
2. Open the application in your browser.
3. Upload a PDF using the sidebar file uploader.
4. Wait for document processing and embedding generation to finish.
5. Enter a question related to the document.
6. Submit the question.
7. Review the generated answer.
8. Compare the response with the original document when verification is needed.

For meaningful results, use text-based PDFs containing extractable text. Scanned documents may require OCR support, which is not included in the initial implementation.

## 14. Configuration and Environment Variables

The application uses environment variables to separate configuration from source code.

| Variable         | Purpose                                  |
| ---------------- | ---------------------------------------- |
| `OPENAI_API_KEY` | Authenticates requests to the OpenAI API |

Additional configuration options can be introduced as the application grows, including model selection, chunk size, overlap, retrieval count, and vector database location.

## 15. Current Scope and Limitations

The initial version focuses on PDF-based question answering.

The following limitations should be considered:

* Only PDF uploads are supported by the current interface.
* The quality of answers depends on PDF text extraction and retrieval relevance.
* Scanned PDFs may require optical character recognition.
* The initial implementation retrieves a fixed number of chunks.
* Language model and embedding API calls may incur costs.
* Local vector storage is not equivalent to a managed production database.
* The current implementation does not establish authentication or multi-user access controls.
* Citations to specific pages or source passages need to be added and verified if required.
* Image understanding, tables, CSV ingestion, and other multimodal capabilities are not yet implemented.

These limitations provide clear directions for future development.

## 16. Future Enhancements

The project can be expanded with additional features to improve usability, retrieval quality, and deployment readiness.

### 16.1 Multi-Document Support

Allow users to upload and query multiple documents within a single knowledge base.

### 16.2 Source Citations

Display the source document, page number, and relevant retrieved passages alongside each answer.

### 16.3 Conversation History

Maintain chat history so users can ask follow-up questions without repeatedly entering the full context.

### 16.4 Multiple File Formats

Extend ingestion to support formats such as TXT, CSV, DOCX, and other structured or unstructured documents.

### 16.5 Multimodal Document Processing

Introduce OCR, image extraction, and vision-model integration to support scanned documents, diagrams, and image-based information.

### 16.6 Improved Retrieval

Evaluate alternative chunk sizes, retrieval counts, metadata filters, and reranking strategies to improve the relevance of retrieved content.

### 16.7 Evaluation and Testing

Create a collection of representative questions and reference answers to measure retrieval quality, answer correctness, and unsupported-answer behavior.

### 16.8 Security and Reliability

Add file validation, upload limits, error handling, API-key protection, temporary-file cleanup, and appropriate access controls.

### 16.9 Cloud Deployment

Deploy the application to a suitable hosting platform and configure its secrets, storage, resource limits, and monitoring.

## 17. Potential Applications

The underlying approach can be adapted to multiple real-world scenarios:

* Research paper analysis.
* Technical documentation search.
* Business report exploration.
* Student study material assistance.
* Company policy lookup.
* Product manual question answering.
* Internal knowledge-base search.

The application is intended to assist with information retrieval, not replace professional judgment or independent verification.

## 18. Learning Outcomes

Developing this project provides practical experience with:

* Building an end-to-end Generative AI application.
* Using language-model APIs.
* Designing a RAG pipeline.
* Extracting and processing PDF content.
* Working with vector embeddings.
* Using a vector database for semantic retrieval.
* Integrating LangChain components.
* Developing an interactive application with Streamlit.
* Managing API credentials and environment variables.
* Organizing Python code into reusable modules.
* Preparing an AI project for testing, documentation, and deployment.

## 19. Conclusion

The Enterprise AI Document Intelligence System demonstrates how document processing, semantic retrieval, vector databases, and Large Language Models can be combined to create an interactive question-answering application.

The project establishes a foundation for more advanced document intelligence capabilities, including source citations, multi-document retrieval, multimodal processing, evaluation, and cloud deployment.

By developing and testing these enhancements incrementally, the application can evolve from a local prototype into a more reliable and portfolio-ready Generative AI system.

## 20. References

* [LangChain Documentation](https://python.langchain.com/docs/introduction/)
* [LangChain Retrieval Documentation](https://python.langchain.com/docs/concepts/retrieval/)
* [OpenAI API Documentation](https://platform.openai.com/docs/)
* [Chroma Documentation](https://docs.trychroma.com/)
* [Streamlit Documentation](https://docs.streamlit.io/)
* [Python Documentation](https://docs.python.org/3/)

---

**Project Status:** Initial PDF-based RAG implementation.

**Planned Direction:** Improve source attribution, retrieval quality, testing, multimodal capabilities, and deployment readiness.
