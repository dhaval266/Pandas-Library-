import pandas as pd 

data = {
    "Name":["Ram","Mayur","Shyam","Raj","Rajni","Rahul","Kajal","Shruti"],
    "Age":[28,19,26,21,28,29,30,34],
    "Salary":[40000,25000,35000,39000,45000,51000,52000,50000],
    "Performance Score":[85,90,95,84,75,98,58,84]
}

df = pd.DataFrame(data)

print(df[df["Salary"] > 50000])     #to filter the data with boolean filter and single condition

print(df[(df["Salary"] > 50000) & (df["Age"] > 29)])        #to filter multiple condition

print(df[(df["Salary"] > 45000) | (df["Performance Score"] > 85)])