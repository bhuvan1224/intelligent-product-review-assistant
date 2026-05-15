from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import generate_answer

app = FastAPI(
    title="Intelligent Product Review Assistant API",
    description="RAG-based API for answering product review questions",
    version="1.0"
)


class ReviewQuery(BaseModel):
    question: str
    product: str = "All"


@app.get("/")
def home():
    return {"message": "Intelligent Product Review Assistant API is running"}


@app.post("/ask")
def ask_question(query: ReviewQuery):
    answer = generate_answer(query.question, query.product)
    return {
        "question": query.question,
        "product": query.product,
        "answer": answer
    }
