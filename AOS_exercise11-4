import numpy as np
import math
import random
import statistics as stats
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import norm

X1_data = [float(1)]*30 + [float(0)]*20
X2_data = [float(1)]*40 + [float(0)]*10

B = 1000
Tboot = []

for _ in range(B):
    X1_star = np.random.choice(X1_data,50,replace=True)
    X2_star = np.random.choice(X2_data,50,replace=True)
    Tboot.append(stats.mean(X2_star) - stats.mean(X1_star))

tau = stats.mean(Tboot)
var = stats.variance(Tboot)
se = np.sqrt(var)
c_low, c_upp = np.percentile(Tboot, [5, 95])

print(f"Bootstrap mean of p2-p1: {tau:.5f}")
print(f"Bootstrap standard error: {se:.5f}")
print(f"90% confidence interval: ({c_low:.2f},{c_upp:.2f})")
