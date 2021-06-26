import torch
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


np.random.seed(123)
a = np.random.normal(3,1,1000)
b = np.linspace(0,999,1000)
#plt.hist(a, bins=30)
#plt.show()

plt.subplot(211)
plt.plot(b, a)
plt.subplot(212)
plt.hist(a, bins=30)
plt.show()

f1 = np.mean(a)
f2 = np.std(a)
f3 = stats.skew(a)
f4 = stats.kurtosis(a)
f5 = (f3 ** 2 + 1) / f4
f6 = np.median(a)
f7 = 0
f8 = 0
f9 = f8 - f7
f10 = np.min(a)
f11 = np.max(a)
