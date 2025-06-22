import pandas as pd 

data = {
    "Name":["Ram","Mayur","Shyam","Raj","Rajni","Rahul","Kajal","Shruti"],
    "Age":[28,19,26,21,28,29,30,34],
    "Salary":[40000,25000,35000,39000,45000,51000,52000,50000],
    "Performance Score":[85,90,95,84,75,98,58,84]
}

df = pd.DataFrame(data)

print(df)

# to adding column in data table we simply use df["column name"] = some data

df["bonus"] = df["Salary"] * 0.1

print(df)

# to add column on perticuler position we use insert()

# insert(location,"column name",some data)

df.insert(2,"Leaves",[1,2,2,4,1,0,2,2])
print(df)