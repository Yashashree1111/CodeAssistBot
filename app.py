from langchain_community.llms import Ollama 
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("Chatbot using CodeLlama")
llm = Ollama(model="codellama:7b")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a code assistant. Generate and explain code in the simplest way possible."),
        ("user", "Question: {question}")
    ]
)


input_text=st.text_input("Search the topic u want")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    with st.spinner("Generating response..."):
        st.write(chain.invoke({"question":input_text}))


# if input_text:
#     if prompt:
#         with st.spinner("Generating response..."):
#             st.write_stream(llm.stream(prompt, stop=['<|eot_id|>']))

