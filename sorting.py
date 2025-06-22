# to sort data by name or number like its sort with alphabetic and numeric methods

# to sorting 1 data column we use sort_values()
# df.sort_values(by="column name", True/False, inplace=True/False)  where second placed True/False refer to order in asc for true and des for false 

import pandas as pd 

data = {
    "Name":["Arun","Raj","Axay","Jay"],
    "Age":[18,22,24,24],
    "Salary":[10000,12000,10000,8000]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by="Age",ascending=False,inplace=True)   #to sort a single column
print(df)

df.sort_values(by=["Salary","Age"], ascending=[True,False], inplace=True)   #to sort multiple columns
print(df)