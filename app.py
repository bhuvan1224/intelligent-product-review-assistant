import streamlit as st
from rag_pipeline import generate_answer

st.set_page_config(
    page_title="Intelligent Product Review Assistant",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ Intelligent Product Review Assistant")

st.write("Ask questions about product reviews using AI-powered semantic search.")

product = st.selectbox(
    "Select Product",
    ["All", "Laptop", "Phone", "Headphones"]
)

question = st.text_input(
    "Enter your question",
    placeholder="Example: Is laptop battery good?"
)

if st.button("Get Answer"):

    if question.strip() == "":
        st.warning("Please enter a question")

    else:
        with st.spinner("Generating answer..."):

            answer = generate_answer(question, product)

        st.subheader("Answer")
        st.write(answer)
