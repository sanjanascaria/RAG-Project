from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.chains import RetrievalQA
import os 

def get_rag_chain(model_name: str):

    loader = TextLoader("indian-elephant.txt")
    documents = loader.load()
    
    for doc in documents:
        doc.metadata["source"] = "indian-elephant.txt"

    # split text into smaller parts
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    # converts chunks into vector embeddings
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embedding_model)

    llm = Ollama(model="mistral-nemo:latest")

    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever(), return_source_documents = True)


