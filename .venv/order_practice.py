#拉麵點餐系統
print("歡迎使用拉麵點餐機")
print("(1)鹽味拉麵$220")
print("(2)醬油拉麵$240")
print("(3)豚骨拉麵$280")
flavor = input("請選擇拉麵口味輸入: 1 or 2 or 3 : ")
large = input("是否加大，豚骨口味$50，其他口味$30(輸入: Y or N)")
eggs = input("是否要加糖心蛋 $30(輸入: Y or N)")
pork = input("是否要加叉燒 $60(輸入: Y or N)")
price = 0
if flavor=="1":
    price+=220
elif flavor=="2":
    price+=240
else:
    price=280
if large=="Y":
    if flavor=="3":
        price+=50
    else:
        price+=30
if eggs=="Y":
    price+=30
if pork=="Y":
    price+=60

print(f"總金額為: {price}元"+" ,謝謝您的光臨")






#測驗一
# num = int(input("請輸入一個整數: "))
# if num%2==0:
#     print("偶數")
# else:
#     print("奇數")

#測驗二 BMI計算機改良
# height = float(input("請輸入您的身高(公分):\n"))
# weight = float(input("請輸入您的體重(公斤):\n"))
# height/=100
# bmi=weight/height**2
# bmi =round(bmi,1)
# # f string 功能是在字串裡面使用其他的資料型態，用法 {變數}
# if bmi>25:
#     print(f"您的BMI是:{bmi}，，體重需要控制")
# elif 20<bmi<25:
#     print(f"您的BMI是:{bmi}，健康")
# else:
#     print(f"您的BMI是:{bmi}，體重過輕")



