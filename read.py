import pandas as pd


# to read csv files use pd.read_csv("file path",encoding="-")

db = pd.read_csv("pandas\sales_data_sample.csv",encoding="latin1")      #it can be encoded in two option one is latin1 and other is utf-8
print(db)


# to read excel file we use pd.read_excel("filepath")

df = pd.read_excel("pandas\SampleSuperstore.xlsx")
print(df)


# to read json formated data we use pd.read_json("filepath")

df = pd.read_json("pandas\sample_Data.json")
print(df)