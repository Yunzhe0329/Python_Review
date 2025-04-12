#綜合健康計算機
#包含計算BMI、BMR(基礎代謝率)以及TDEE(總熱量消耗)
#BMI = 體重/身高**2
#BMR 男性 : 66+(13.7 * 體重(kg) + 5 * 身高(公分) - 6.8*年齡)
#女性 : 655+(9.6 * 體重(kg) + 1.8 * 身高(公分) - 4.7*年齡)
# TDEE 久坐、幾乎沒運動 BMR*1.2 、 每周低強度運動 BMR*1.375 、 每周中強度運動BMR*1.55、每周高強度運動BMR*1.725
# 勞力密集工作或是每天高強度訓練 BMR*1.9


def bmi_caculator(height, weight):
    height /= 100
    bmi = weight/height**2
    bmi = round(bmi, 1)
    return bmi

def bmr_caculator(gender, height, weight, age) :
    if gender=="男":
        bmr = 66+(13.7 * weight + 5 * height - 6.8*age)
    else:
        bmr = 655+(9.6 * weight + 1.8 * height - 4.7*age)
    bmr = round(bmr, 2)
    return bmr
def tdee_caculator(gender, height, weight, age , times):


    bmr = bmr_caculator(gender, height, weight,age)
    if type =="1":
        tdee = bmr*1.2
    elif type=="2":
        tdee = bmr*1.375
    elif type == "3":
        tdee = bmr * 1.55
    elif type=="4":
        tdee = bmr*1.725
    else:
        tdee = bmr * 1.9
    tdee = round(tdee,2)
    return tdee



print("歡迎使用綜合健康計算機")
print("(1)計算BMI")
print("(2)計算BMR")
print("(3)計算TDEE")
item = input("請選擇想要計算的項目")
height = int(input("請輸入您的身高(公分): "))
weight = int(input("請輸入您的體重(公斤): "))
gender = input("請輸入您的性別 (男 or 女)")
age = int(input("請輸入你的年齡 :"))
print("(1)久坐、幾乎沒運動\n")
print("(2)每周低強度運動 1~3天\n")
print("(3)每周中強度運動 3~5天\n")
print("(4)每周高強度運動 6~7天\n")
print("(5)勞力密集工作或是每天高強度訓練\n")
times = input("請輸入您的運動量(輸入 1~5 )")
if item=="1":
    bmi=bmi_caculator(height, weight)
    print(f"您的BMI為 : {bmi}")
elif item=="2":
    bmr=bmr_caculator(gender, height, weight, age)
    print(f"您的BMR為 : {bmr}")
else:
    tdee = tdee_caculator(gender, height, weight, age , times)
    print(f"您的TDEE為 : {tdee}")