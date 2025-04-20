import pandas as pd
df = pd.read_csv("data.csv")
#use to_string() to print the entire DataFrame.
# print(df)
# print(df.to_string())
#設定 Pandas 顯示 DataFrame 時 最多顯示的列數（rows）上限為 9999 行，讓你可以完整看到大量資料，而不是被自動省略成 ...
pd.options.display.max_rows = 9999
# print(df)

#Pandas Read JSON :
df2 = pd.read_json("openData.json")
print(df2)