from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import MessagesPlaceholder
from langchain.chains import create_history_aware_retriever
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from flipkart.data_ingestion import data_ingestion

from dotenv import load_dotenv
import os
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model = "llama-3.3-70b-versatile", temperature=0.5)

chat_history = []
store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k":3})
    retriever_prompt = ("Given a chat history and the latest user question which might reference context in the chat history,"
    "formulate a standalone question which can be understood without the chat history."
    "Do NOT answer the question, just reformulate it if needed and otherwise return it as is."
    )

    contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
    ("system", retriever_prompt),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    ]
    )
    history_aware_retriever = create_history_aware_retriever(model, retriever, contextualize_q_prompt)

    PRODUCT_BOT_TEMPLATE = """
    You are an expert product recommendation assistant for an e-commerce platform. Your role is to answer customer queries based on product reviews, titles, and chat history.
    Instructions:
    - Always identify and mention the full product name being referred to, even if the user uses pronouns like "they" or "it".
    - Use prior chat history to accurately resolve references to previously mentioned products.
    - Your responses should be factual, concise, and grounded in the provided context.
    - Stay on topic and ensure every answer is relevant to the product features, performance, or comparisons discussed.

    CONTEXT:
    {context}

    QUESTION: {input}

    YOUR ANSWER:

    """

    qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", PRODUCT_BOT_TEMPLATE),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ]
    )
    question_answer_chain = create_stuff_documents_chain(model, qa_prompt)

    chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key = "input",
    history_messages_key = "chat_history",
    output_messages_key = "answer",
    )

    return chain_with_memory

if __name__ == "__main__":
    vstore,insert_ids = data_ingestion("done")
    conversational_rag_chain = generation(vstore)
    answer = conversational_rag_chain.invoke(
        {"input":"Can you suggest a nice pair of earphones?"},
        config = {
            "configurable" : {"session_id" : "abhi142s"}
        },
    )["answer"]
    print(answer)
    answer1 = conversational_rag_chain.invoke(
        {"input":"Are they waterproof?"},
        config = {
            "configurable" : {"session_id" : "abhi142s"}
        },
    )["answer"]
    print(answer1)
    answer2 = conversational_rag_chain.invoke(
        {"input":"What was my previous question?"},
        config = {
            "configurable" : {"session_id" : "abhi142s"}
        },
    )["answer"]
    print(answer2)
