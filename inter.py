import pandas as pd 

data = {
    "Time":[1,2,3,4,5,6,7,8,9],
    "Values":[10,20,None,40,50,None,70,80,None]
}

df = pd.DataFrame(data)
print(df)

df["Values"] = df["Values"].interpolate(method="linear",axis=0,inplace=True)
print(df)

