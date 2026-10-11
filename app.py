import os
import streamlit as st
from dotenv import load_dotenv
from data_processor import ingest_and_embed_pdf
from rag_chain import create_rag_system

load_dotenv()

st.set_page_config(
    page_title="Enterprise AI Document Analysis",
    page_icon="📄",
    layout="wide"
)

st.title("Enterprise AI Document Analysis System")
st.caption("Ask questions about your PDF documents using Gemini and RAG.")

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_name" not in st.session_state:
    st.session_state.document_name = None

with st.sidebar:
    st.header("Document Upload")

    uploaded_file = st.file_uploader(
        "Upload a PDF document",
        type=["pdf"]
    )

    if uploaded_file is not None:
        if uploaded_file.name != st.session_state.document_name:
            os.makedirs("temp", exist_ok=True)

            pdf_path = os.path.join("temp", uploaded_file.name)

            try:
                with open(pdf_path, "wb") as file:
                    file.write(uploaded_file.getbuffer())

                with st.spinner("Processing your PDF..."):
                    retriever = ingest_and_embed_pdf(pdf_path)
                    st.session_state.rag_chain = create_rag_system(retriever)
                    st.session_state.document_name = uploaded_file.name
                    st.session_state.messages = []

                st.success("PDF processed successfully!")

            except Exception as error:
                st.session_state.rag_chain = None
                st.session_state.document_name = None
                st.error(f"Unable to process the PDF: {error}")

    if st.session_state.document_name:
        st.info(f"Current document: {st.session_state.document_name}")

    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()

if st.session_state.rag_chain is None:
    st.info("Upload a PDF from the sidebar to start asking questions.")

else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_query = st.chat_input("Ask a question about your document...")

    if user_query:
        st.session_state.messages.append({
            "role": "user",
            "content": user_query
        })

        with st.chat_message("user"):
            st.markdown(user_query)

        with st.chat_message("assistant"):
            with st.spinner("Searching your document..."):
                try:
                    response = st.session_state.rag_chain.invoke({
                        "input": user_query
                    })

                    answer = response["answer"]
                    st.markdown(answer)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer
                    })

                except Exception as error:
                    st.error(f"Unable to generate an answer: {error}")