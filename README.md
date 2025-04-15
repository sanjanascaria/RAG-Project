# 🧠 Ask Notes App – RAG with FastAPI + Ollama
This is a lightweight Retrieval-Augmented Generation (RAG) app built with FastAPI and LangChain, powered by Ollama for local LLMs. You can ask questions based on the content of a .txt file, and even choose which model to use.

🚀 Features
📄 Loads a local text file as knowledge base

🔎 Chunks and embeds documents using HuggingFaceEmbeddings + FAISS

💬 Queries the vectorstore with a FastAPI endpoint

🤖 Supports dynamic model selection via Ollama

🐳 Dockerized for easy deployment

## 🧪 Local Run (without Docker)

Run the app using `uvicorn main:app --reload`.

## 🐳 Run with Docker

1. Build the image `docker build -t ask-notes-app .`
2. Run the image `docker run -p 8000:8000 ask-notes-app`
