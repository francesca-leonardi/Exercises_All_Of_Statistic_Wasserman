import numpy as np
import math
import random
import statistics
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm

mu = 5
n = 100
X_data = np.random.normal(mu,1,n)

mu_prior = 1
mu_post = (np.sum(X_data) + mu_prior)/(n+1)
var_post = 1/(n+1)
sd_post = np.sqrt(var_post)

x = np.linspace(mu_post - (3*sd_post),mu_post + (3*sd_post),100)
y_x = stats.norm.pdf(x, mu_post, sd_post)

plt.plot(x,y_x, label = 'Posterior densisty for mu')

B = 100

X_post = np.random.normal(mu_post,sd_post,B)

plt.hist(X_post, bins = 30, density = True, label = 'Sample for the posterior densisty')
plt.legend()
plt.show()

theta_sample = np.exp(X_post)
plt.hist(theta_sample, bins = 30, density = True, label = 'Sample for the posterior density of theta = e^mu')
plt.show()
