#  summary topic has the summerised value of the data like
# df["column name"].sum()
# df["column name"].min()
# df["column name"].max()
# df["column name"].mean()

import pandas as pd 


data = {
    "Name":["Arun","Raj","Axay","Jay"],
    "Age":[18,22,24,24],
    "Salary":[10000,12000,10000,8000]
}

df = pd.DataFrame(data)
print(df)

print(df["Age"].sum())
print(df["Salary"].mean())