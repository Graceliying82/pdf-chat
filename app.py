import streamlit as st
import openai
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
from langchain.vectorstores import Pinecone

from handlers.userinput import handle_userinput
from database import pinecone_db
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

from constants import OPENAI_API_KEY, INDEX_NAME
from views.htmlTemplates import css
from utils.inputs.pdf import parse_pdfs

from icecream import ic


# documentation for CharacterTextSplitter:
# https://python.langchain.com/en/latest/modules/indexes/text_splitters/examples/character_text_splitter.html
def get_text_chunk(text):
    # use text_splitter to split it into documents list
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
    )
    chunks = text_splitter.split_text(text)

    # (variable) docs: List[Document]
    docs = [Document(page_content=text) for text in chunks]
    return docs


# embedding using openAI embedding. Warn: This will cost you money
def get_vectorstore_openAI(data):
    # default model is:text-embedding-ada-002
    embeddings = OpenAIEmbeddings()



    #   will not to use vector in memory today.
    #    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    pinecone_db.create_index(INDEX_NAME)
    # to get more information, you can look at this page
    # https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/pinecone

    vectorstore = Pinecone.from_documents(data, embedding=embeddings, index_name=INDEX_NAME)
    return vectorstore


# embedding using instructor-xl with your local machine for free you can find more details at:
# https://huggingface.co/hkunlp/instructor-xl This code snippet demo how to use other model for text embedding. Will
# not use this for my project. But will keep this here for reference. def get_vectorstore(text_chunks): embeddings =
# HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl") vectorstore = FAISS.from_texts(texts=text_chunks,
# embedding=embeddings) return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    ic(f"conversation_chain is {conversation_chain}")
    return conversation_chain


def main():
    openai.api_key = OPENAI_API_KEY

    # Set up pinecone database

    # set up basic page
    st.set_page_config(page_title="Chat With multiple PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    # initial session_state in order to avoid refresh
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat based on PDF you provided :books:")
    user_question = st.text_input("Ask a question about your documents:")

    if user_question:
        handle_userinput(user_question)

    # Define the templates

    with st.sidebar:
        st.subheader("Your PDF documents")
        pdf_docs = st.file_uploader("Upload your pdfs here and click on 'Proces'", accept_multiple_files=True)
        # if the button is pressed
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                data = parse_pdfs(pdf_docs)
                ic('pdfs have been reading into data')

                # Use loader and data splitter to make a documentlist
                doc = get_text_chunk(data)
                ic(f'text_chunks are generated and the total chucks are {len(doc)}')

                # create vector store
                vectorstore = get_vectorstore_openAI(doc)

    embeddings = OpenAIEmbeddings()
    INDEX_NAME = 'pdfchat'
    print(f'{INDEX_NAME}')
    vectorstore = Pinecone.from_existing_index(index_name=INDEX_NAME, embedding=embeddings)
    # create conversation chain
    st.session_state.conversation = get_conversation_chain(vectorstore)
    ic('conversation chain created')


# to run this application, you need to run "streamlit run app.py"
if __name__ == '__main__':
    main()
