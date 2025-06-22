import pandas as pd

df = pd.read_json("pandas/sample_Data.json")

print(df.info())    #to get information of data

df = pd.read_csv("pandas/output.csv")

print(df.info())