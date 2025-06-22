import pandas as pd 

data = {
    "Name":["Ram",None,"Shyam","Raj","Rajni","Rahul","Kajal","Shruti"],
    "Age":[28,None,26,21,28,29,30,34],
    "Salary":[40000,None,35000,39000,45000,51000,52000,50000],
    "Performance Score":[85,None,95,84,75,98,58,84]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())  #return data frame of true-false

# to know how much values is missing simply add some() like .isnull().sum()

print(df.isnull().sum())