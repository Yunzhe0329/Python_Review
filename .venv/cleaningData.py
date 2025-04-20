import pandas as pd
df = pd.read_csv("data.csv")
#Empty cells => can potentially give you a wrong result when you analyze data
#(1)dropna()Return a new Data Frame with no empty cells, inplace設定True會直接從原始資料移除empty cell，若確定不需要保留原始資料可以使用來節省memory
# empty_cells = df.dropna()
# print(empty_cells)
#Replace Empty Values
#(2)fillna() method allows us to replace empty cells with a value
#Replace NULL values with the number 130
# df.fillna(130, inplace = True)
#Replace Only For Specified Columns
# df.fillna({"Calories": 130}, inplace = True)
#(3)Most common way to replace empty cell => Using Mean, Median, or Mode
# x = df["Calories"].mean()
# x = df["Calories"].median()
#Mode = the value that appears most frequently.
x = df["Calories"].mode()[0]
print(x)
df.fillna({"Calories": x}, inplace= True)
print(df.to_string())