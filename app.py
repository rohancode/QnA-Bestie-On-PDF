import os
import sys
from dotenv import load_dotenv

from langchain.llms import Replicate
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain

import streamlit as st
import pinecone

def main():
    # Load environment variables from .env file
    load_dotenv()

    # App framework basic
    st.set_page_config(page_title="QnA Bestie on PDF")
    logo = "logo.jpg"
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:    
        st.image(logo, use_column_width='auto')
    st.title("QnA Bestie on PDF")
    about_text = (
        "The app takes a PDF and allows user to ask questions and provides corresponding answers extracted from PDFs. The AI behind the app is the llama2 model. While the model is open source and offers free usage, the challenge lies in the computationally expensive setup, therefore in this project replicate API has been used which has a free API quota. Upload your file and get your answers today!"
    )
    st.write(about_text)
    uploaded_file = st.file_uploader("Upload PDF and wait a bit (top right of the screen...)", type=["pdf"])
    
    # st.write("Checkpoint 1")
    
    # Pinecone
    pinecone.init(api_key=os.environ['PINECODE_API_TOKEN'], environment=os.environ['PINECONE_ENV'])

    if uploaded_file is not None:
        # Load PDF
        file_path = uploaded_file.name
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        # st.write("Checkpoint 2")
        
        # Embeddings
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        embeddings = HuggingFaceEmbeddings()
        index_name = os.environ['PINECONE_INDEX']
        index = pinecone.Index(index_name)
        vectordb = Pinecone.from_documents(texts, embeddings, index_name=index_name)
        # st.write("Checkpoint 3")
        
        # Llms
        llm = Replicate(
        model=os.environ['REPLICATE_MODEL_ENDPOINT13B'],
        input={"temperature": 0.1, "max_length": 3000}
        )

        qa_chain = ConversationalRetrievalChain.from_llm(
        llm,
        vectordb.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True
        )
        # st.write("Checkpoint 4")

        # Q&A Chat
        user_prompt = st.text_input("Question for the PDF?", value="", key="user_prompt")
        chat_history=[]
        if user_prompt:
            result = qa_chain({'question': user_prompt, 'chat_history': chat_history})
            st.write(f"{result['answer']}")
            chat_history.append((user_prompt, result['answer']))
            # st.write("Checkpoint 5.1")
        # st.write("Checkpoint 5.2")
        
        if os.path.exists(file_path):
            os.remove(file_path)
        # st.write("Checkpoint 6")
    
    st.header("Contact Me")
    contact_text = (
        "Feel free to reach out to me if you have any questions, suggestions, or just want to connect!"
    )
    st.write(contact_text)
    st.markdown("[Email](mailto:rohan.rathore93@gmail.com)")
    st.markdown("[GitHub](https://github.com/rohancode)")
    # st.write("Checkpoint 7")

if __name__ == "__main__":
    main()