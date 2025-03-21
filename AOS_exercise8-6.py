import numpy as np
import math
import random
import statistics
import matplotlib.pyplot as plt
from scipy.stats import norm

n = 100
mu = 5
th = np.e**mu

X = np.random.normal(5,1,n)
th_hat = np.e**(statistics.mean(X))

B = 10000
T_boot = [0]*B

for i in range(B):
    X_star = np.random.choice(X, n, replace = True)
    T_boot[i] = np.e**(statistics.mean(X_star))
    
se = np.sqrt(statistics.variance(T_boot))
normal = [th_hat - 2*se, th_hat + 2*se]
print(normal)

plt.hist(T_boot, bins = 30, density = True)

x = np.linspace(4.7,5.3,1000)
y_x = norm.pdf(x,5,0.1)
b = np.exp(x)
y_b = (1/b)*norm.pdf(np.log(b),5,0.1)

plt.plot(b, y_b)
plt.show()
