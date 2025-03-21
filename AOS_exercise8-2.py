import numpy as np
import math
import random
import statistics

n = 50
Y = np.random.standard_normal(n)
X = [math.e**y for y in Y]

m = statistics.mean(X)
se = statistics.pvariance(X)
T = 1/n * sum((x-m)**3 / se for x in X)

B = 100
Tboot = [0]*B

for i in range(B):
    X_star = np.random.choice(X, n)
    m_star = statistics.mean(X_star)
    se_star = np.sqrt(statistics.pvariance(X_star))
    skew_star = 1/n * sum((x-m_star)**3 / se_star for x in X_star)
    Tboot[i] = skew_star
    
se = np.sqrt(statistics.pvariance(Tboot))
normal = [T - 2*se, T + 2*se]
percentile = np.quantile(Tboot, [0.025,0.975])
pivotal = [2*T - np.quantile(Tboot, 0.975), 2*T - np.quantile(Tboot, 0.025)]

print(T, normal, pivotal, percentile)
