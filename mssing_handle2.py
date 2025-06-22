import pandas as pd 

data = {
    "Name":["Ram",None,"Shyam","Raj","Rajni","Rahul","Kajal","Shruti"],
    "Age":[28,None,26,21,28,29,30,34],
    "Salary":[40000,None,35000,39000,45000,51000,52000,50000],
    "Performance Score":[85,None,95,84,75,98,58,84]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum())

# if we care about the missing value and fill it we use fillna(value,inplace=True/False)
# inplace for real data changes applied if true else make new data frame 

df.fillna({"Name":"Mayur","Age":22,"Salary":35000,"Performance Score":89.99}, inplace=True) 
# we can use conditionle value alos like 
# df["Age"].fillna(df.["Age"].mean(), inplace=True)
# df["Salary"].fillna(df["Salary"].max(), inplace=True)
print(df)

print(df.isnull())
print(df.isnull().sum())