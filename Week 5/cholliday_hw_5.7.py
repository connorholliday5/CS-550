import numpy as np
from scipy.stats import binom

n_heads_required = 100
n_tosses_check = 224  
p = 0.5                

# T >= 225 means fewer than 100 heads in first 224 tosses
prob_theoretical = binom.cdf(n_heads_required - 1, n_tosses_check, p)

print(f"Theoretical Probability: {prob_theoretical:.6f}")

