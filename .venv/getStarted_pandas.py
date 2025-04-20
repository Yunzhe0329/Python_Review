import pandas as pd

#Series => 一維資料(像是一個欄位)
a = [1, 3, 5]
print(a)

#Labels : if nothing else is specified, the values are labeled with their index number
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)

#key-value object like a dictionary
# calories = {"day1": 420, "day2": 700, "day3": 500}
# myvar = pd.Series(calories, index=["day1", "day2"]) #use index can get specify data
# print(myvar)

#--------------------------------------------------------------------------------------
#DataFrame二維資料表（像是 Excel 表格）
data = {
    "Calories" : [420, 700, 500, 350],
    "Duration" :[50, 40, 45, 50]
}
# df = pd.DataFrame(data)
#search for specific row (series)
# print(df.loc[0])
# #using [], the result is a Pandas DataFrame.
# print(df.loc[[1, 2]])
#named index
df = pd.DataFrame(data, index = ["day1", "day2", "day3", "day4"])
print(df)
#return value's data type => <class 'pandas.core.series.Series'>
print(df.loc["day3"])

