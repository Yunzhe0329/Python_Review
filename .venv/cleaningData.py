import pandas as pd
df = pd.read_csv("fitness_data.csv")
#Empty cells => can potentially give you a wrong result when you analyze data
#(1)dropna()Return a new Data Frame with no empty cells, inplace設定True會直接從原始資料移除empty cell，若確定不需要保留原始資料可以使用來節省memory
empty_cells = df.dropna()
# print(empty_cells)
#Replace Empty Values
#(2)fillna() method allows us to replace empty cells with a value
#Replace NULL values with the number 130
#df.fillna(130, inplace = True)
#Replace Only For Specified Columns
# df.fillna({"Calories": 130}, inplace = True)
#(3)Most common way to replace empty cell => Using Mean, Median, or Mode
#x = df["Calories"].mean()
# x = df["Calories"].median()
#Mode = the value that appears most frequently.
# x = df["Calories"].mode()[0]
# print(x)
# df.fillna({"Calories": x}, inplace= True)
# print(df.to_string())


#Cleaning Data of Wrong Format

#(1) wrong date
#format="%Y/%m/%d"可以指定格式(處理起來速度更快、效能更好)
# df["Date"] =pd.to_datetime(df["Date"], format='mixed')
#根據 Date 欄位是否為缺失值（NaN）來刪除該列，其他欄位就算有 NaN 也不影響 ; subset(指定欄位)、inplace設為True會直接修改原始資料
# df.dropna(subset=["Date"], inplace=True)
# print(df.to_string())

#Fixing Wrong Data => row7        450  '2020/12/08'    104       134     253.3
#(1) 直接修改資料
# df.loc[7, "Duration"] = 45
# print(df.loc[7])
#(2)替換成固定數值
#Loop through all values in the "Duration" column.If the value is higher than 120, set it to 120
# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#         df.loc[x, "Duration"] =120
# print(df.to_string())
# (3) 直接刪除整筆資料
# for x in df.index:
#     if df.loc[x, "Duration"] >120:
#         df.drop(x, inplace = True)
# print(df.to_string())

#Remove duplacates
# print(df.duplicated()) # row 12 is a duplicate data
df.drop_duplicates(inplace = True)
print(df.duplicated())
