import os
from dotenv import load_dotenv

from langchain import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chain import LLMChain


import streamlit as st

# Load environment variables from .env file
load_dotenv()

# App framework
st.title("LangChain Table Extract")
prompt = st.text_input("What is the Prompt")

# Llms
llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.7, "max_length":64}) #exp to avoid timeout

# Show result
if prompt:
    response = llm(prompt)
    st.write(response)