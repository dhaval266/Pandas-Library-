import pandas as pd 

data = {
    "Name":["Ram","Mayur","Shyam","Raj","Rajni","Rahul","Kajal","Shruti"],
    "Age":[28,19,26,21,28,29,30,34],
    "Salary":[40000,25000,35000,39000,45000,51000,52000,50000],
    "Performance Score":[85,90,95,84,75,98,58,84]
}

df = pd.DataFrame(data)
print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)

# to remove perticuler column we use drop(columns = ["column name"] , inplace=True)  inplace is nothing but the changes in real data if it false it returns new data frame
df.drop(columns=["Bonus"], inplace = True)
print(df)

# to delete multiple columns simply add name at list box .drop(columns=["column1","column2"], inplace = True)

