from numpy import kaiser
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('gshare.csv')
#x=df.counter_Bits
y=df.gcc_miss_rate
z=df.new_bits

k = [27.81,
23.56,
19.94,
16.95,
14.46,
12.53]

x=[7,
8,
9,
10,
11,
12]



y1=[28.95,
24.96,
20.84,
18,
15.05,
13.4]

y2=[31.1,
27.53,
23.47,
19.88,
17.06,
14.47]

y3 = [29.53,
25.49,
21.22,
17.75,
15.16]

y4=[22.55,
18.83,
15.69]

y5=[16.28]


plt.plot(x, k,marker='.')
plt.plot(x,y1,marker='.')
plt.plot(x,y2,marker='.')
plt.plot(x[1:],y3,marker='.')
plt.plot(x[3:],y4,marker='.')
plt.plot(x[-1],y5,marker='.')


plt.title('gcc_trace ,Bimodal')
plt.xlabel('Counter Bits')
plt.ylabel('Miss Prediction Rate')
plt.grid()
plt.show()