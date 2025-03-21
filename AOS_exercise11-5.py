import numpy as np
import math
import random
import statistics as stats
from scipy.stats import beta
import matplotlib.pyplot as plt

X = [0,1,0,1,0,0,0,0,0,0]
ones = sum(X)
zeros = len(X) - ones

x = np.linspace(0,0.8,1000)

plt.figure(figsize=(8, 6))
plt.plot(x,[beta.pdf(x0, ones + (1/2),zeros + (1/2)) for x0 in x], label='Posterior density for prior Beta(1/2,1/2)')
plt.plot(x,[beta.pdf(x0, ones + 1,zeros + 1) for x0 in x], label='Posterior density for prior Beta(1,1)')
plt.plot(x,[beta.pdf(x0, ones + 10,zeros + 10) for x0 in x], label='Posterior density for prior Beta(10,10)')
plt.plot(x,[beta.pdf(x0, ones + 100,zeros + 100) for x0 in x], label='Posterior density for prior Beta(100,100)')
plt.legend()
plt.show()
