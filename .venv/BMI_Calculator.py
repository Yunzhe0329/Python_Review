#BMI 計算機
height = float(input("請輸入您的身高(公分):\n"))
weight = float(input("請輸入您的體重(公斤):\n"))
height/=100
bmi=weight/height**2
bmi =round(bmi,1)
# f string 功能是在字串裡面使用其他的資料型態，用法 {變數}
print(f"您的BMI是:{bmi}")
