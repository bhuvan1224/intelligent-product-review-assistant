# Intelligent Product Review Assistant

A GenAI-powered RAG application that analyzes product reviews and answers user questions using semantic search and LLMs.

## Features

- Product review question answering
- Semantic search using ChromaDB
- RAG pipeline for grounded responses
- Metadata filtering by product
- Groq LLM integration
- Streamlit frontend
- FastAPI backend with Swagger docs

## Tech Stack

Python, Streamlit, FastAPI, ChromaDB, LangChain, Groq, Pandas

## Project Workflow

User Question → ChromaDB Semantic Search → Relevant Reviews → Groq LLM → Final Answer

## How to Run

```bash
pip install -r requirements.txt
python vector_store.py
python -m streamlit run app.py
