import pandas as pd


def load_reviews(path="data/reviews.csv"):

    df = pd.read_csv(path)

    print("Dataset Loaded Successfully")
    print(df.head())

    return df


if __name__ == "__main__":

    data = load_reviews()
