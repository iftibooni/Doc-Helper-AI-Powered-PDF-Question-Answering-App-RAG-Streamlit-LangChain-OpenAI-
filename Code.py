from dotenv import load_dotenv
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
import streamlit as st
import pprint


load_dotenv()
#step 1: Load the PDF file
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        background-color: #eaf0fb;
        color: #222222; /* Set text color to dark */
    }
    .stFileUploader>div>div {background-color: #eaf0fb;}
    .stButton>button {background-color: #4F8BF9; color: white;}
    .stMarkdown {font-size: 1.1em;}
    </style>
    """, unsafe_allow_html=True)

st.title("📄 Doc Helper")
st.markdown("#### Upload your PDF and ask any question about its content!")

uploaded_file = st.file_uploader("Choose a PDF document", type=["pdf"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    retriever = vectorstore.as_retriever(search_type='similarity',search_kwargs={"k": 1})

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

    st.success("Document uploaded and processed! You can now ask questions below.")

    query = st.text_input("🔎 Ask a question about your document:")

    if query:
        relevant_docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in relevant_docs])

        prompt = PromptTemplate(
            template="""
              You are a helpful assistant.
              Answer ONLY from the provided document context.
              If the context is insufficient, just say you don't know.

              {context}
              Question: {question}
            """,
            input_variables = ['context', 'question']
        )
        formatted_prompt = prompt.format(context=context, question=query)

        response = llm.invoke(formatted_prompt)
        st.markdown("#### 📝 Answer:")
        st.info(response.content)

