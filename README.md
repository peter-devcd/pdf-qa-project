# pdf-qa-project
It;s a simple pdf document summarizer(college project)

# 📄 PDF Question Answering System

This is an AI-based application that allows users to upload a PDF and ask questions about its content.

## 🚀 Features
- Upload PDF files
- Extract text automatically
- Ask questions from document
- Get AI-based answers

## 🧠 Technology Used
- Python
- Streamlit
- Sentence Transformers
- FAISS / Numpy

## 📌 How it works
This project uses Retrieval-Augmented Generation (RAG) technique:
1. Converts text into embeddings
2. Matches user query with document
3. Returns the most relevant answer

## ▶️ Run locally
```bash
streamlit run app.py
