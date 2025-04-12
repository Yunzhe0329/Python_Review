from PIL.ImageOps import scale
from numpy import random
import numpy as np
#generate random number Note : this is truly random (cannot be predicted ! )
x = random.randint(100)
print(x)

# float number(0~1)
y = random.rand()
print(y)

#generate random array(first value means the range of numbers & second one means the shape of array)
arr = random.randint(100, size=(5))
arr_2D = random.randint(100, size=(2,3))
print(arr)
print(arr_2D)

#choice() method allow to generate a random value based on an array of values ,also can use size parameter to create arrays
valueChoice = random.choice([1, 3, 5, 7, 9], size=(2, 3))
print(valueChoice)

#Radom data distribution : a list of all possible values, and how often each value occurs Note : sum of probability must be 1
prob_rdnumber = random.choice([1, 3, 5, 7, 9], p=[0.3, 0.4, 0.2, 0, 0.1], size = (100))
print(prob_rdnumber)
#Random permutation() & shuffle() permutation => 類似copy()的效果，並不會影響到原本的array ; shuffle()=> View的效果，會直接操作原本的Array
blocks = np.array([1, 2, 3, 4, 5])
new_blocks = random.permutation(blocks)
print(blocks)
print(new_blocks)

#--------------------------------------------------------------------------

#Seaborn : 可用來產生精緻的圖表 vs Matplotlib 產生基本的圖
import matplotlib.pyplot as plt
import seaborn as sns
#Plotting a Displot(分布圖)
#sns.histplot([0, 1, 2, 3, 4, 5], kde=True) #新版的直方圖，kde是用來畫平滑線
sns.displot([0, 1, 2, 3, 4, 5], kde=True) #可以畫很多圖、排版圖，想一次畫多張圖可以使用
#plt.show()

#Normal ditribution(別名 : Gaussian Distribution) e.g. IQ、Height、grade are classic examples
#The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.(中間高兩邊低)
# normal() , has three parameters loc(Mean), scale(stander deviation), size(shape of array)
#normalDis = random.normal(loc=1, scale=2, size=(2, 3))
sns.displot(np.random.normal(size=(1000)), kde=True)
#plt.show()
#print(normalDis)


#--------------------------------------------------------------------------
#統計相關的知識

#Binomail distribution二項分配(is a Discrete(離散) Distribution) e.g.丟硬幣
# n = numbers of trials ; p = probability of occurance of each trial(丟硬幣機率是5050) ; size = shape of the array
#從中央極限定理出發，當 n 很大時，成功次數的可能值也很多，分布形狀會越來越像鐘形曲線，也就是常態分布
#bio = random.binomial(n = 10, p = 0.5, size=(10))
#print(bio)
sns.displot(random.binomial(n = 10, p = 0.5, size=(10)))
#plt.show()
#when n is enough, this biomail distribution will close to normal distribution
data = {
    "normal": random.normal(loc=50, scale=5, size= 1000),
    "biomial":random.binomial(n=100, p=0.5, size= 1000)
}
sns.displot(data, kde=True)
# plt.show()

#Poisson Distribution : 在一段時間內，某件事情會發生幾次？
#poisson() : two parameters => lam(平均單位時間發生次數) - rate or known number of occurrences e.g. 2 for above problem ; size - The shape of the returned array.
# poisson_dis = random.poisson(lam=2, size=10)
# print(poisson_dis)
sns.displot(random.poisson(lam=2, size=1000))
# plt.show()