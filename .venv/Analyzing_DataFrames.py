import pandas as pd
df = pd.read_csv("data.csv")
#沒有給定參數，預設是5筆資料
print(df.head())
print(df.tail())
#gives you more information about the data set
print(df.info())
