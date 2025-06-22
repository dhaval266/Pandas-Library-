#  to identify the data set first check the rows of the data

# to view data by starting and ending we use head() and tail()

# head(n) number of rows , by default its 5 rows present at u if u dont valued n

# tail(n) number of rows , by default its 5 rows present at u if u dont values n

import pandas as pd

df = pd.read_json("pandas/sample_Data.json")

print(df.head(10)) #desplay 10 top rows

print(df.tail(10)) #desplay 10 bottom rows


# without n value 

print(df.head())

print(df.tail())