from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import create_retrieval_chain
from langchain import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate


def create_rag_system(retriever):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    system_prompt = (
        "You are an AI document analysis assistant. "
        "Answer the user's question using only the information "
        "provided in the retrieved document context. "
        "If the answer cannot be found in the context, clearly say "
        "that the document does not provide enough information. "
        "Do not invent facts or make unsupported claims.\n\n"
        "Retrieved context:\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])

    question_answer_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    rag_chain = create_retrieval_chain(
        retriever,
        question_answer_chain
    )

    return rag_chain