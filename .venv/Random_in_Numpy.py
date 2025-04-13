from PIL.ImageOps import scale
from numpy import random
import numpy as np
#generate random number Note : this is truly random (cannot be predicted ! )
x = random.randint(100)
# print(x)

# float number(0~1)
y = random.rand()
# print(y)

#generate random array(first value means the range of numbers & second one means the shape of array)
arr = random.randint(100, size=(5))
arr_2D = random.randint(100, size=(2,3))
# print(arr)
# print(arr_2D)

#choice() method allow to generate a random value based on an array of values ,also can use size parameter to create arrays
valueChoice = random.choice([1, 3, 5, 7, 9], size=(2, 3))
#print(valueChoice)

#Radom data distribution : a list of all possible values, and how often each value occurs Note : sum of probability must be 1
prob_rdnumber = random.choice([1, 3, 5, 7, 9], p=[0.3, 0.4, 0.2, 0, 0.1], size = (100))
#print(prob_rdnumber)
#Random permutation() & shuffle() permutation => 類似copy()的效果，並不會影響到原本的array ; shuffle()=> View的效果，會直接操作原本的Array
blocks = np.array([1, 2, 3, 4, 5])
new_blocks = random.permutation(blocks)
#print(blocks)
#print(new_blocks)

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
# data = {
#     "normal": random.normal(loc=50, scale=5, size= 1000),
#     "biomial":random.binomial(n=100, p=0.5, size= 1000)
# }
# sns.displot(data, kde=True)
# plt.show()

#Poisson Distribution : 在一段時間內，某件事情會發生幾次？
#poisson() : two parameters => lam(平均單位時間發生次數) - rate or known number of occurrences e.g. 2 for above problem ; size - The shape of the returned array.
# poisson_dis = random.poisson(lam=2, size=10)
# print(poisson_dis)
sns.displot(random.poisson(lam=2, size=1000))
# plt.show()

#Uniform Distribution(均勻分布)e.g.丟骰子(每個面出現機率相同) : Used to describe probability where every event has equal chances of occuring
#uniform() Three parameters : low - lower bound - default 0 .0 ; high - upper bound - default 1.0. ; size - The shape of the returned array
# uni_dis = random.uniform(size=(2, 3)) #result [[0.488783   0.92023012 0.67650396][0.89340886 0.14489299 0.63507321]]
# print(uni_dis)
sns.displot(random.uniform(size=1000), kde="kde")
# plt.show()

#Logistic Distribution : Logistic Distribution is used to describe growth.
#Used extensively in machine learning in logistic regression, neural networks etc.
#logistic() : 3 parameters , loc - mean, where the peak is. Default 0. ; scale - standard deviation, the flatness of distribution. Default 1.;size - The shape of the returned array.
# log_dis = random.logistic(loc = 1, scale = 2, size=(2, 3))
# print(log_dis)
sns.displot(random.logistic(size=1000), kde = "kde")
# plt.show()

#difference with normal distribution : logistic distrbution are like normal distribution but with more area under the tails
# data = {
#     "Normal Distibution": random.normal(scale = 2, size=1000),
#     "Logistic Distribution":random.logistic(size=1000)
# }
# sns.displot(data, kde="kde")
# plt.show()

#Multinomial Distribution(多項分布，一件事會產生多種結果) ; Biomial 二項分布 (只有成功和失敗兩種結果)
#multinomial() 3 parameters, n - number of times to run the experiment. ; pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll); size - The shape of the returned array.
#假設有 3 種顏色（機率分別為 0.2、0.5、0.3），試驗 10 次 (結果是每個類別出現的次數)
mul_dis = random.multinomial(n=10, pvals=[0.2, 0.5, 0.3])
# print(mul_dis)

# Exponential distribution is used for describing "time till next event" e.g. failure/success
# 常常和 Poisson 分布成對使用
# exponential() , 2 parameters , scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0 ; size - The shape of the returned array.

# exp_dis = random.exponential(scale = 2, size = (2, 3))
# print(exp_dis)
sns.displot(random.exponential(size = 1000), kde="kde")
# plt.show()

#Chi Square Distribution 卡方分配 : is used as a basis to verify the hypothesis(連續型的機率分布)，用來衡量「實際結果」與「理論期望」之間有多大的差距
# it has 2 parameters : df :degree of freedom, size - The shape of the returned array.
#你有好幾個「標準常態分布（平均 0、標準差 1）」的數值，然後你把它們平方再加總起來，這個結果就會符合卡方分布，即degree of freedom(自由度) : df越大越接近normal distribution
# chi_dis = random.chisquare(df = 2, size = (2, 3))
# print(chi_dis)
# sns.displot(random.chisquare(df = 1, size = 1000),kde = "kde")
# plt.show()

#Rayleigh Distribution（雷利分布） : 一種跟「方向、距離、通訊、風速」有關的機率分布，常常出現在工程與物理領域中 ; 從 0 開始慢慢上升、然後下降的曲線（右偏鐘形）
#當一個變數是兩個互相獨立、且都服從標準常態分布的變數的平方和的平方根時，這個變數就服從 Rayleigh 分布 => 我從 X 軸與 Y 軸隨機走，每次都是標準常態，那我走出的距離服從 Rayleigh 分布！
# It has 2 parameters: scale - (standard deviation) decides how flat the distribution will be default 1.0). ; size - The shape of the returned array.
# ray_dis = random.rayleigh(scale = 2, size=(2, 3))
# print(ray_dis)
# sns.displot(random.rayleigh(size = 1000), kde="kde")
# plt.show()

#Pareto Distribution（帕累托分布）=> 80/20法則 一種右偏的分布(少數人或少數東西，佔據了大多數的資源或影響力)
# 2 parameters : a - shape parameter. ; size - The shape of the returned array.
#α 越小 → 尾巴越長 → 出現「極大值」的機率越高
#α 越大 → 尾巴越短 → 分布越集中，極端值比較少(穩定)
# pareto_dis = random.pareto(a = 2, size = (2, 3))
# print(pareto_dis)
# sns.displot(random.pareto(a = 2, size = 1000), kde="kde")
# plt.show()

#Zipf Distribution（齊普夫分布）: 在語言學、社會學、網路流量、城市人口、甚至 YouTube 熱門影片中都出現
#一種 "離散型(discrete0"的長尾分布 : 「排名越前的東西，出現得越頻繁，而且按某種比例快速下降」
# 2 parameters : a - distribution parameter. ; size - The shape of the returned array.
#a是形狀參數 s（控制前幾名的集中程度），越大 → 前幾名越集中、越極端（越長尾）
zipf_dis = random.zipf(a = 2, size = (2, 3))
#選出小於 10 的數值，展平為一維再畫圖
sns.displot(zipf_dis[zipf_dis<10])
plt.show()
# print(zipf_dis)
