import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('slr04.xls')
x = df['X']
y = df['Y']
xmean = np.mean(x)
ymean = np.mean(y)

f1 = lambda x,y: ((x - xmean) * (y - ymean))
f2 = lambda x: (x - xmean)**2

sumf1 = sum(f1(x,y))
sumf2 = sum(f2(x))


m = sumf1/sumf2
b = ymean - m * xmean

# m,b can also be found simply by using the built in polyfit function in numby library
# m,b = np.polyfit(x, y, deg=1)

f = lambda x: m*x + b

plt.plot(x, f(x), c="k")
plt.xlabel('Unemployment rate for adult males')
plt.ylabel('Unemployment rate for adult females')
plt.title('National Unemployment Rates')
plt.scatter(x,y)
plt.show()
