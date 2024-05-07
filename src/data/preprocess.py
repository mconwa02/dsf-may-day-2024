import os
import pandas as pd

PATH = r"C:\dev\data\dsf"
df = pd.read_csv(os.path.join(PATH, "product_info_simple_final_train.csv"))
print(df.head())
print(df.info())