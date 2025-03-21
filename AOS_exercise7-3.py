import numpy as np
import math
import random
import scipy.stats as stats
from statsmodels.distributions.empirical_distribution import ECDF

n_simulations = 1000
count = 0

for _ in range(n_simulations):
    N = 100
    sample = np.random.normal(0,1,N)  # Generate standard normal samples
    ecdf = ECDF(sample)  # Compute empirical CDF
    
    alpha = 0.05
    epsilon = np.sqrt(np.log(2/alpha) / (2*N))  # Compute confidence band width
    
    mean = np.mean(sample)  # Alternative to 1/N * sum(sample)
    se = np.std(sample, ddof=1) / np.sqrt(N)  # Standard error of the mean
    
    x_vals = np.sort(sample)  # Sort sample points
    ecdf_vals = ecdf(x_vals)  # Evaluate ECDF at x_vals
    
    confidence = [np.maximum(ecdf_vals - epsilon, 0), np.minimum(ecdf_vals + epsilon, 1)]

    true_cdf = stats.norm.cdf(x_vals, loc=0, scale=1)  # True normal CDF at sample points

    # Use element-wise logical operators & instead of and
    if np.all((true_cdf >= confidence[0]) & (true_cdf <= confidence[1])):
        count += 1

print(count)
