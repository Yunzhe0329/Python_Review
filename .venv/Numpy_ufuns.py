# ufunct => universal functions
#NumPy 就像是一個超厲害的數學小幫手，可以很快幫我們算一大堆數字(ndarray object)
#ufuncs 就是大計算機，可以「一次對很多數字做同一件事」
from itertools import product

import numpy as np
from Numpy_practice import newarr

#Vectorization（向量化）: NumPy 的函數（特別是 ufuncs）在底層是透過 C-level loop / BLAS / LAPACK 等高效實作，能大幅提升速度

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
# list3 = []
#用for-loop效率比較差
# for i, j in zip(list1, list2):
#     list3.append(i + j)
# print(list3)
#用Numpy 的 array處理會比較快,add() numpy built-in function to do this(much faster)
list3 = np.add(list1, list2)
print(list3)

#---------------------------------------------------------------------------------------------------------------------

#create your own ufunc =>frompyfunc(func, nin, nout) :用來將 Python 的函數轉成 ufunc（universal function） 的工具
def myAdd(x, y):
    return(x + y)

myAdd = np.frompyfunc(myAdd, 2, 1)
print(type(myAdd))
print(type(np.concatenate)) #if it is not a ufunc, it will return another type
print(myAdd([1, 2, 3, 4],[4, 5, 6, 7] ))


#---------------------------------------------------------------------------------------------------------------------
# Simple Arithmetic（簡單算術運算）=> element-wise ,元素對元素的運算
#add()
arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]

# newarr = np.add(arr1, arr2)
# newarr = np.subtract(arr1, arr2)
# newarr = np.multiply(arr1, arr2)
# newarr = np.divide(arr1, arr2)
# newarr = np.power(arr1, arr2)

#both mod() & remainder() 都是餘數
# newarr = np.mod(arr2, arr1)
# newarr = np.remainder(arr2, arr1)
#Quotient and Mod 商數和餘數，用divmod()可以做同時計算
# newarr = np.divmod(arr2, arr1)#output : (array([6, 3, 2, 2, 2]), array([0, 1, 2, 1, 0]))
arr3 = [-1, -10, -3, -2]
# newarr = np.abs(arr3)
# print(newarr)

#---------------------------------------------------------------------------------------------------------------------
# Rounding Decimals（小數四捨五入）
# a = np.array([3.14159, 2.71828, -1.618, -2.9])

# print("原始：", a)
# print("Rounding：", np.round(a, 2))   # 四捨五入到小數點後 2 位
# print("Floor：", np.floor(a))      # 無條件捨去
# print("ceil：", np.ceil(a))        # 無條件進位
# print("Truncation：", np.trunc(a))      # 直接去掉小數
# print("fix：", np.fix(a))          # 朝 0 取整（正數像 trunc，負數像 ceil）
#Logs
# x = np.array([1, 10, 100, 1000])
#
# print("自然對數 log:", np.log(x))      # 底為 e
# print("log10（常用對數）:", np.log10(x)) # 底為 10
# print("log2（以 2 為底）:", np.log2(x))  # 底為 2

#NumPy Summations : 把一堆數字「加起來」的動作
# a = np.array([1, 2, 3, 4])
# #sum是總和, axis	指定加總的「方向」，例如 axis=0 表示對 column 加總 ;keepdims	是否保留原本的維度（預設 False）
# print(np.sum(a))  # ➜ 10
# b = np.array([[1, 2],
#               [3, 4]])
# print(np.sum(b))           # ➜ 10（全部加起來）
# print(np.sum(b, axis=0))   # ➜ [4 6]（對 column 加總）
# print(np.sum(b, axis=1))   # ➜ [3 7]（對 row 加總）
# #cumsum : 累加和
# x = np.array([1, 2, 3, 4])
# print(np.cumsum(x))  # ➜ [1 3 6 10]
# print(np.sum(b, axis=1, keepdims=True))
# ➜ [[3]
#     [7]]

#product : 乘積計算
# a = np.array([2, 3, 4])
# print(np.prod(a))
# arr_1 = np.array([1, 2, 3, 4])
# arr_2 = np.array([5, 6, 7, 8])
# #Find the product of the elements of two arrays
# print(np.prod([arr_1, arr_2]))
# #product over axis ; axis=0 => column
# print(np.prod([arr_1, arr_2], axis=1))
# #Cummulative Product
# print(np.cumprod(a))

#Difference 差值運算 : 計算一個陣列「相鄰元素之間的差值
#parameter : n :做多次差值（差的差）
# arr = np.array([10, 15, 25, 5])
# newarr = np.diff(arr, n = 2) #[  5 -30]
# print(newarr)

#Lowest Common Multiple,LCM 最小公倍數
# num1 = 4
# num2 = 6
# x = np.lcm(num1, num2)
# print(x)
# #計算多個數的 LCM（用 reduce()）
# nums = [4, 6, 8]
# print(np.lcm.reduce(nums))

#Greatest Common Devisor,GCD 最大公因數
# num1 = 6
# num2 = 9
# x = np.gcd(num1, num2)
# print(x)
# #GCD in arrays
# nums = [20, 8, 32, 36, 16]
# print(np.gcd.reduce(nums))
#------------------------------------------------------------------------

# #Trigonometric Functions
# #np.pi，NumPy 提供的常數 π（約 3.14159）
# # x = np.sin(np.pi/2)
# # print(x)
# # arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
# # z = np.sin(arr)
# # print(z)
# #Convert Degrees Into Radians : radians values are pi/180 * degree_values.
# arr = np.array([90, 180, 270, 360])
# x = np.deg2rad(arr)
# print(x)
# #Radians to Degrees
# arr_rad = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
# z = np.rad2deg(arr_rad)
# print(z)
# #Hypotenues
# base = 3
# perp = 4
# y = np.hypot(base, perp)
# print(y)

#------------------------------------------------------------------------
#Hyperbolic Functions雙曲線函數 :sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values
# x = np.sinh(np.pi/2)
# print(x)
# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
# x = np.cosh(arr)
# print(x)

#NumPy Set Operations 集合運算

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
#unique() 對陣列去重並排序
x = np.unique(arr)
print(x)
#union1d()聯集：合併不重複元素
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
#intersection1d() 找交集 ，預設會先做Unique去重複再找交集
#parameter :assume_unique=True or False (True就代表你告訴NumPy：「我保證傳進來的兩個陣列都沒有重複值」可以省略 unique() 的處理，執行速度更快！)
newarr_intersec = np.intersect1d(arr1, arr2)
print(newarr_intersec)
#setdiff1d()差集 => 在 a 不在 b 的值(有先後順序!)
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr_diff = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr_diff)
# Symmetric Difference=> setxor1d() 對稱差集 : 僅出現在其中一邊的值
newarr_symmetricdiff = np.setxor1d(set1, set2)
print(newarr_symmetricdiff)
