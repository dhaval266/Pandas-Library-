# to concatenate two data frame by vertically(row wise) or horizontlly(column wise)
# pd.concate([df1,df2], axis=0/1, ignore_index=True/False)
# [df1,df2] = data frames
# axis= 0-row wise, 1-column wise
# ignore_index=True for reset index of combine data frame which will creat


import pandas as pd 

customer1 = pd.DataFrame({
    "Id":[1,2,3,4,5,6],
    "Name":["Ramesh","Suresh","Dharmesh","Rakesh","Kalpesh","Dinesh"]
})

customer2 = pd.DataFrame({
    "Id":[8,9,10,11,12,13,14],
    "Name":["Dherya","Sunil","Raj","Alpesh","Dilip","Lakhan","Lokesh"]
})

concated = pd.concat([customer1,customer2], axis=0, ignore_index=True)
print(concated)

concated = pd.concat([customer1,customer2], axis=1, ignore_index=True)
print(concated)