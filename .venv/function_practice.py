#測驗一
#函式碰到return就會直接回傳，不會往下執行
def find_max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

max =find_max(10,20,30)
print(max)

#測驗2
def find_min(num1, num2, num3):
    if num1<=num2 and num1<=num3:
        return num1
    elif num2<=num1 and num2<=num3:
        return num2
    else:
        return num3

def max_min(num1, num2, num3):
    if type(num1)!= int or type(num2)!= int or type(num3)!= int:
        return "請輸入整數"
    else:
        return find_max(num1, num2, num3)-find_min(num1, num2, num3)

result = max_min(100,50,2)
print(result)

