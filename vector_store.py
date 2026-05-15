import chromadb
from data_preprocessing import load_reviews


def create_vector_store():
    df = load_reviews()

    client = chromadb.PersistentClient(path="vector_db")

    collection = client.get_or_create_collection(name="product_reviews")

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

    print("Vector store created successfully")
    print("Total reviews stored:", collection.count())


if __name__ == "__main__":
    create_vector_store()
