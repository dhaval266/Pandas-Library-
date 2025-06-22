#  in pandas we can group a perticuler category or item 

# using groupby() method

import pandas as pd 

data = {
    "Name":["Dhaval","Raj","Chand","Sunil","Suman","Rensi","Devansh","Dev"],
    "Age":[25,21,25,22,24,22,20,21],
    "Salary":[15000,25000,21000,23000,14000,18000,19000,20000]
}

df = pd.DataFrame(data)

# for single group
grouped = df.groupby("Age")["Salary"].mean()    #groupby("Column name to group")["Column name to opration"].operation
print(grouped)

# for multiple columns group
grouped = df.groupby(["Age","Name"])["Salary"].mean()
print(grouped)