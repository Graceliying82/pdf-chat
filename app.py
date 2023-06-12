import streamlit as st
import openai
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTemplates import css, bot_template, user_template
from PIL import Image

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# documentation for CharacterTextSplitter:
# https://python.langchain.com/en/latest/modules/indexes/text_splitters/examples/character_text_splitter.html
def get_text_chunk(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks

#embedding using openAI embedding. Warn: This will cost you money
def get_vectorstore_openAI(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

#embedding using instructor-xl with your local machine for free
#you can find more details at: https://huggingface.co/hkunlp/instructor-xl
def get_vectorstore_openAI(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(text=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory = memory
    )
    return conversation_chain

def main():
    ##############################################################################
    #load openai api_key from .evn
    load_dotenv()
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    
    ##############################################################################
    #set up basic page
    st.set_page_config(page_title="Chate With multiple PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    #initial session_state in order to avoid refresh
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    st.header("Chat based on PDF you provided :books:")
    st.text_input("Ask a question about your documents:")

    # Define the image paths
    human_image = Image.open('human.png')
    robot_image = Image.open('robot.png')

# Define the templates

    st.write(user_template.replace("{{MSG}}", 'Hello, I am a human'), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}",'Hello, I am a robot'), unsafe_allow_html=True)
    with st.sidebar:
        st.subheader("Your PDF documents")
        pdf_docs = st.file_uploader("Upload your pdfs here and click on 'Proces'", accept_multiple_files= True)
        #if the button is pressed
        if st.button("Process"):
            with st.spinner("Processing"):
                #get pdf text
                raw_text = get_pdf_text(pdf_docs)

                #get the text chunks
                text_chunks = get_text_chunk(raw_text)

                #create vector store
                vectorstore = get_vectorstore_openAI(text_chunks)

                #create converstion chain
                st.session_state.conversation = get_conversation_chain(vectorstore)
    



# to run this application, you need to run "streamlit run app.py"
if __name__ == '__main__':
    main()