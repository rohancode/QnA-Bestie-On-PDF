import os
from dotenv import load_dotenv

from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory 


import streamlit as st

# Load environment variables from .env file
load_dotenv()

# App framework
st.title("LangChain Table Extract")
prompt = st.text_input("What is the Prompt?")

# Prompts Templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = "Translate the following English word in German: {topic}"
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template = 'Make me a new sentence in Geman with the word: {title}'
)

# Memory
memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')

# Llms
llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.7, "max_length":64}) #exp to avoid timeout
title_chain = LLMChain(llm=llm, prompt=title_template,verbose=True, output_key='title', memory=memory)
script_chain = LLMChain(llm=llm, prompt=script_template,verbose=True, output_key='script', memory=memory)
sequencial_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=['topic'], output_variables=['title', 'script'], verbose=True)

# Show result
if prompt:
    response = sequencial_chain({'topic':prompt} )
    st.write(response['title'])
    st.write(response['script'])

    with st.expander('Message Histroy'):
        st.info(memory.buffer)