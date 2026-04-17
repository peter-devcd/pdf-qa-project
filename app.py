import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np
import re

st.set_page_config(page_title="Mr.PDF", layout="wide")

st.title("📄 Mr.PDF - Question Answering System (FREE)")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    st.success("✅ PDF uploaded successfully!")

    # Read PDF
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    st.subheader("📜 Extracted Text Preview:")
    st.write(text[:1000])

    # Load model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Chunking
    chunk_size = 500
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    embeddings = model.encode(chunks)

    st.success("🧠 Embeddings Ready!")

    # Question input
    query = st.text_input("❓ Ask a question from the PDF:")

    if query:
        query_embedding = model.encode([query])

        similarities = np.dot(embeddings, query_embedding.T).flatten()
        top_indices = similarities.argsort()[-3:][::-1]

        st.subheader("📌 Answer:")

        best_sentence = ""
        max_score = -1

        for i in top_indices:
            chunk = chunks[i]
            sentences = chunk.split(".")

            for sentence in sentences:
                sentence_embedding = model.encode([sentence])
                score = np.dot(sentence_embedding, query_embedding.T)[0][0]

                if score > max_score:
                    max_score = score
                    best_sentence = sentence.strip()

     
        
        # 🔥 Clean answer properly
        clean_answer = best_sentence.replace("\n", " ")
        clean_answer = clean_answer.replace("•", "")
        clean_answer = clean_answer.strip()

        # Remove unwanted prefixes (like names, numbers)
        match = re.search(r"(C\+\+.*)", clean_answer)

        if match:
            clean_answer = match.group(1)

            st.write(clean_answer)

        