import os
import chromadb
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from data_preprocessing import load_reviews

load_dotenv()


def get_collection():
    client = chromadb.PersistentClient(path="vector_db")
    collection = client.get_or_create_collection(name="product_reviews")

    if collection.count() == 0:
        df = load_reviews()

        for index, row in df.iterrows():
            collection.add(
                documents=[row["review"]],
                metadatas=[
                    {
                        "product": row["product"],
                        "rating": int(row["rating"])
                    }
                ],
                ids=[str(index)]
            )

    return collection


def retrieve_reviews(question, product=None):
    collection = get_collection()

    if product and product != "All":
        results = collection.query(
            query_texts=[question],
            n_results=3,
            where={"product": product}
        )
    else:
        results = collection.query(
            query_texts=[question],
            n_results=3
        )

    return results


def generate_answer(question, product=None):
    results = retrieve_reviews(question, product)

    reviews = results["documents"][0]
    metadata = results["metadatas"][0]

    context = ""

    for review, meta in zip(reviews, metadata):
        context += f"Product: {meta['product']}, Rating: {meta['rating']}, Review: {review}\n"

    prompt = f"""
You are an Intelligent Product Review Assistant.

Answer the user's question using only the product reviews given below.

Product Reviews:
{context}

User Question:
{question}

Give a clear, simple, grounded answer.
If the reviews do not contain enough information, say that clearly.
"""

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":
    answer = generate_answer("Is laptop battery good?", product="Laptop")
    print(answer)
