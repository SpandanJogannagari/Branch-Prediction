from cProfile import label
from numpy import kaiser
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('gshare.csv')
x=df.counter_Bits
y=df.gcc_miss_rate
z=df.new_bits
x2=[]
x4=[]
x6=[]
x8=[]
x10=[]
x12 =[]
y2=[]
y4=[]
y6=[]
y8=[]
y10=[]
y12=[]
for i in range(0,27):
    if(z[i]==2):
        y2.append(y[i])
        x2.append(x[i])
    elif(z[i]==4):
        y4.append(y[i])
        x4.append(x[i])
    elif(z[i]==6):
        y6.append(y[i])
        x6.append(x[i])
    elif(z[i]==8):
        y8.append(y[i])
        x8.append(x[i])
    elif(z[i]==10):
        y10.append(y[i])
        x10.append(x[i])
    elif(z[i]==12):
        y12.append(y[i])
        x12.append(x[i])
    
plt.plot(x2,y2,marker='.',label='2')
plt.plot(x4,y4,marker='.',label='4')
plt.plot(x6,y6,marker='.',label='6')
plt.plot(x8,y8,marker='.',label='8')
plt.plot(x10,y10,marker='.',label='10')
plt.plot(x12,y12,marker='.',label='12')
plt.title('gcc_trace ,gshare')
plt.xlabel('PC Bits')
plt.ylabel('Miss Prediction Rate')
plt.legend()
plt.grid()
plt.show()



