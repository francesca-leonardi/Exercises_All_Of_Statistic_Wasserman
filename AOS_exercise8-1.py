import numpy as np
import math
import statistics
import random
import scipy.stats as stats

B = 1000     # iterations of the bootstrap
n = 10     # size of the sampling

X = np.random.uniform(0,1,n) # data
T = statistics.median(X)

Tboot = [0]*B
for i in range(0,B):
    Xstar = np.random.choice(X, n)
    Tboot[i] = statistics.median(Xstar)

se = np.sqrt(statistics.pvariance(Tboot))
print(se)
