import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('smith.csv')
x=df.counter_Bits
y=df.perl_miss_rate

plt.plot(x, y,marker='.')
plt.title('perl_trace ,Smith')
plt.xlabel('Counter Bits')
plt.ylabel('Miss Prediction Rate')
plt.grid()
plt.show()