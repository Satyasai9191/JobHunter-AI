from dotenv import load_dotenv
from langchain_groq import ChatGroq
from app.config import MODEL_NAME
from app.prompts import SYSTEM_PROMPT
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model = MODEL_NAME
)

def build_question(question):
    return [
    SystemMessage(
        content = SYSTEM_PROMPT
    ),

    HumanMessage(
        content= question
    )

    ]

def ask_ai(question):

    messages = build_question(question)
    response = llm.invoke(messages)
    return response.content