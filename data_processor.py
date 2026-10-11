import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

load_dotenv()

CHROMA_DB_DIR = "./chroma_db"
EMBEDDING_MODEL = "text-embedding-3-small"

def ingest_and_embed_pdf(pdf_path):
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    if not documents:
        raise ValueError("The PDF contains no extractable pages.")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)

    if not chunks:
        raise ValueError(
            "No extractable text was found in the PDF. Scanned PDFs may require OCR."
        )

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    db = Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings
    )
    db.add_documents(chunks)

    return db.as_retriever(search_kwargs={"k": 3})