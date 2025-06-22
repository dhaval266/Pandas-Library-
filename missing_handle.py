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

# if we dont care about the missing value and remove it we use dropna(axis=0/1,inplace=True/False) where axis stand for rows and columns
# if axis = 0 its rows and 1 for columns, inplace for real data changes applied if true else make new data frame 

df.dropna(inplace=True) #by default axis set to 0   
print(df)