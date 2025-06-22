# this method use to merge two or more columns where there key is matched 

# pd.merge(df1,df2, on="Column name", how="type of join")

import pandas as pd 

customer = pd.DataFrame({
    "Id":[1,2,3,4,5,6],
    "Name":["Ramesh","Suresh","Dharmesh","Rakesh","Kalpesh","Dinesh"]
})

order = pd.DataFrame({
    "Id":[1,2,4,5,6,7],
    "Amount":[250,350,475,480,500,560]
})

df_merge = pd.merge(customer,order, on="Id", how="inner")   #inner join
print(df_merge)

df_merge = pd.merge(customer,order, on="Id", how="outer")   #outer join
print(df_merge)

df_merge = pd.merge(customer,order, on="Id", how="left")   #left join
print(df_merge)

df_merge = pd.merge(customer,order, on="Id", how="right")   #right join
print(df_merge)

df_merge = pd.merge(customer,order, how="cross")   #cross join where on is not include
print(df_merge)