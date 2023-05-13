import streamlit as st
from pdf_handler import extract_pdf_text
from chatbot import answer_question

st.title("AI PDF Chatbot")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    pdf_text = extract_pdf_text(uploaded_file)
    question = st.text_input("Ask a question about the PDF:")
    
    if question:
        answer = answer_question(question, pdf_text)
        st.write(answer)

