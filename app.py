import os
from dotenv import load_dotenv
import sys
import pinecone
from langchain.llms import Replicate
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain

# Load environment variables from .env file
load_dotenv()

pinecone.init(api_key=os.environ['PINECODE_API_TOKEN'], environment=os.environ['pinecone_env'])

# Load PDF
loader = PyPDFLoader(os.environ['PDF_PATH'])
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings()
index_name = os.environ['pinecone_index']
index = pinecone.Index(index_name)
vectordb = Pinecone.from_documents(texts, embeddings, index_name=index_name)
print("Checkpoint C1")

# # App framework
# st.title("LangChain Table Extract")
# prompt = st.text_input("What is the Prompt?")

# # Prompts Templates
# title_template = PromptTemplate(
#     input_variables = ['topic'],
#     template = "Translate the following English word in German: {topic}"
# )

# script_template = PromptTemplate(
#     input_variables = ['title'],
#     template = 'Make me a new sentence in Geman with the word: {title}'
# )

# # Memory
# memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')

# # Llms
llm = Replicate(
    model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
    input={"temperature": 0.1, "max_length": 3000}
)
print("Checkpoint C2")
# Set up the Conversational Retrieval Chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm,
    vectordb.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True
)
print("Checkpoint C3")
# Start chatting with the chatbot
chat_history = []
while True:
    query = input('Prompt: ')
    if query.lower() in ["exit", "quit", "q"]:
        print('Exiting')
        sys.exit()
    result = qa_chain({'question': query, 'chat_history': chat_history})
    print('Answer: ' + result['answer'] + '\n')
    chat_history.append((query, result['answer']))
print("Checkpoint C4")
# # Show result
# if prompt:
#     response = sequencial_chain({'topic':prompt} )
#     st.write(response['title'])
#     st.write(response['script'])

#     with st.expander('Message Histroy'):
#         st.info(memory.buffer)