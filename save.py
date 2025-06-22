import pandas as pd

# to save data to file in any formate there is an option and method according to formate 

data = {
    "Name":["Ram","ketan","dhaval"],
    "Age":[25,24,25],
    "City":["delhi","mumbai","Gujrat"]
}

df = pd.DataFrame(data)     #for make encoding to data we make datafram first of the data and then we save it
print(df)

df.to_csv("pandas/output.csv",index=False)  #to store as csv file use to_csv("filepath and name to store")


df.to_excel("pandas/output.xlsx",index=False)   #to store as excel formate we use .to_excel("file path and name")


df.to_json("pandas/output.json",index=False)    #to store as json formate we use .to_json("file path and name")