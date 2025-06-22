# there are two question you have to face 

#  how big ur data set
# what is ur columns names

# to solve that questions we have two methods 
# ṣhape
# columns

import pandas as pd 

data = {
    "Name":["Ram","Mayur","Shyam","Raj","Rajni","Rahul","Kajal","Shruti"],
    "Age":[28,19,26,21,28,29,30,34],
    "Salary":[40000,25000,35000,39000,45000,51000,52000,50000],
    "Performance Score":[85,90,95,84,75,98,58,84]
}

df = pd.DataFrame(data)
print(df)

print(df.shape)

print(df.columns)