# -*- coding: utf-8 -*-
"""DAP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W0PSgWdO0F4HoWXemLzbvehEcFNWT-ru
"""

import numpy as np
A = np.array([[1, 2], [3, 4]])

# creating second matrix
B = np.array([[4, 5], [6, 7]])

print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)

# adding two matrix
print("Addition of two matrix")
print(np.add(A, B))

import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
a=np.zeros((3,3),dtype=int)
print(a)
b=np.ones((2,2),dtype=int)
print(b)
a_range=np.arange(10)
print(a_range)
reshaped_arr=arr.reshape(5,1)
print(reshaped_arr)
sliced_arr=arr[2:4]
print(sliced_arr)

arr1=np.array([1,2,3,4,5])
print(arr1)
arr2=np.array([3,4,5,6,7])
print(arr2)
result=arr1+arr2
print(result)
arr1=np.array([1,2,3,4,5])
print(arr1)
b=arr1+3
print(b)

a1=np.array([1,2,3,4,5])
print(a1)
a2=np.array([3,4,5,6,7])
print(a2)
a3=np.vstack(a1+a2)
print(a3)
a1=np.array([1,2,3,4,5])
print(a1)
a2=np.array([3,4,5,6,7])
print(a2)
a3=np.stack(a1+a2)
print(a3)
c=np.array([1,2,3,4,5,6,7,8])
b=np.split(c,4)
print(b)

a1=np.array([[1,2,3,4],[5,6,7,8]])
print(a1)
b=a1.T
print(b)

b1=np.array([[1,2],[3,4]])
print(b1)
b2=np.array([[5,6],[7,8]])
print(b2)
c1=np.dot(b1,b2)
print(c1)
d1=np.linalg.eig(c1)
print(d1)
e1=np.array([[1,2,3],[4,5,6]])
print(e1)
e2=np.array([[1,2,3],[4,5,6]])
print(e2)
e3=np.sum(e1+e2)
print(e3)

e1=np.array([[1,2,3],[4,5,6]])
print(e1)
e4=np.sum(e1,axis=0)
print(e4)
e5=np.sum(e1,axis=1)
print(e5)
arr11=np.array([1,2,3,4,5])
print(arr11)
arr22=np.mean(arr11)
print(arr22)
arr33=np.median(arr11)
print(arr33)
arr44=np.var(arr11)
print(arr44)
arr55=np.std(arr11)
print(arr55)

data=np.loadtxt("/content/data.txt")
print(data)
data=np.loadtxt("/content/data.txt",dtype=int)
print(data)
data=np.savetxt("/content/data2.txt",data)
print(data)

import matplotlib.pyplot as plt
a=np.array([1,2,3,4,5,6,7,8,9,10])
plt.plot(a)

import pandas as pd
a=["uma","jeshitha","mounika","supriya","poojitha"]
r=pd.Series(a,index=[38,23,50,25,15])
print(r)

df=pd.read_csv("/content/cr_tweets.csv")
print(df)

df=pd.read_csv("/content/data.txt",sep=" ")
print(df)
print(df.loc[1])

df=pd.read_excel("/content/salesworkload.xlsx",sheet_name=1)
print(df)

df=pd.read_csv("/content/cr_tweets.csv")
mv=df["bookmarkCount"].mean()
df = df.fillna(mv)
print(mv)

df=df.drop_duplicates()
print(df)
df.head(8)
df.tail(9)
df.shape

from google.colab import drive
drive.mount('/content/drive')

df=pd.read_csv("/content/cr_tweets.csv")
tail=df.tail(10)
shape=df.shape
print(shape)

df=pd.read_csv("/content/cr_tweets.csv")
a=df.head(8)
b=df.tail(9)
shape=df.shape
print(shape)
df=pd.concat([a,b],axis=0)
df.to_csv("df.csv")
print(df)

df=pd.read_csv("/content/cr_tweets.csv")
print(df.groupby(['bookmarkCount'])['quoteCount'].count())

import numpy as np
import matplotlib.pyplot as plt
runs=np.array([100,50,91,78,89,25,34,19,99,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.scatter(runs,w,color='blue')
plt.title('INDvsAUS_score')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
tigar=np.linspace(-2*np.pi,2*np.pi,50)
print(tigar)
plt.plot(tigar,np.sin(tigar),color='black')
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
runs=np.array([100,50,91,78,89,25,34,19,99,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.plot(runs,w,color='blue')
plt.title('INDvsAUS_score')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
overs =np.arange(5,50,5)
overs_a =np.arange(5,30,5)
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,92,110,151,])
wicket =np.array([12,32,96])
plt.plot(overs,runs_i,color='blue',label='India')
plt.plot(overs_a,runs_a,color='yellow',label='Aus')
plt.legend(loc='best')
plt.show()

import pandas as pd
a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]
profit_a=[a[i]-a[i-1] for i in range(1,len(a))]
profit_b=[b[i]-b[i-1] for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='orange',linewidth='3',label='CompanyA',marker='>',ms='15',mec='k')
plt.legend(loc='best')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='blue',linestyle= 'dotted',label='CompanyB',marker='H')
plt.legend(loc='best')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
overs =np.arange(5,50,5)
overs_a =np.arange(5,30,5)
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,92,110,151,])
wicket =np.array([12,32,96])
plt.subplot(2,1,2)
plt.plot(overs,runs_i,color='blue',label='India')
plt.legend(loc='best')
plt.subplot(2,1,1)
plt.plot(overs_a,runs_a,color='yellow',label='Aus')
plt.legend(loc='best')
plt.show()

a=np.array([25,60,5,10])
labe=["CSE","Python","Pandas","Numpy"]
plt.pie(a,labels =labe)
c=["lightblue","lightgreen","orange","lightpink"]
plt.pie(a,colors=c)
plt.legend(loc='best')
plt.show()

a=np.array([25,60,5,10])
labe=["CSE","Python","Pandas","Numpy"]
explo=[0.2,0,0,0]
plt.pie(a,labels =labe,explode=explo,startangle=100,textprops={'fontsize':28})
plt.legend(loc='best')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("/content/city_temperature.csv")
print(df)
average_temperature = df['AvgTemperature'].mean()
highest_temperature = df['AvgTemperature'].max()
lowest_temperature =df['AvgTemperature'].min()
threshold=30
days_above_threshold=df[df['AvgTemperature']> threshold].shape[0]
print("Average temperature for the month:", average_temperature)
print("Highest temperature recorded:", highest_temperature)
print("Lowest temperature recorded:", lowest_temperature)
print("Number of days where temperature exceeded", threshold, "degrees Celsius:", days_above_threshold)

df.plot(kind='line',color='black')
plt.title('jan month AvgTemperature')
plt.xlabel('days')
plt.ylabel('temp')
plt.show()

pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.violinplot(x="days",y="total_bill")
sns.scatterplot(x="tip",y="total_bill", data=tips)
plt.title("scatter plot of total Bill vs.Tip")
plt.xlabel("Tip ($)")
plt.ylabel("Total Bill  ($)")
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt

# Load the anscombe dataset
anscombe = sns.load_dataset("anscombe")

# Display the first few rows of the dataset to understand its structure
print(anscombe.head())

# Plot the four datasets in the anscombe dataset
sns.set(style="ticks")
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=anscombe,
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.violinplot(x="day",y="total_bill", data=tips)
plt.title("Distribution of total Bill vs.Tip")
plt.xlabel("Day of the week")
plt.ylabel("Total Bill  ($)")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset("iris")
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("correlation heatmap of iris Dataset")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset("titanic")
correlation_matrix=iris.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("correlation heatmap of iris Dataset")
plt.show()

