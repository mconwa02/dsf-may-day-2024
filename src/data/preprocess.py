import os
import pandas as pd


PATH = r"C:\dev\data\dsf"


def process_data():
    """Collecting data locally"""
    df = pd.read_csv(os.path.join(PATH, "product_info_simple_final_train.csv"))
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])
    df = df.set_index("transaction_date")
    print(df.head())
    print(df.info())


if __name__ == "__main__":
    process_data()
