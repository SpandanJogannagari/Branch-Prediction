import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('bimodal.csv')
x=df.counter_Bits
y=df.perl_miss_rate

plt.plot(x, y,marker='.')
plt.title('perl_trace ,Bimodal')
plt.xlabel('PC Bits')
plt.ylabel('Miss Prediction Rate')
plt.grid()
plt.show()