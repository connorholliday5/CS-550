import numpy as np

lambda_param = 2 
N = 1_000_000     

# For k = 2, P(T1 >= 2*T2) = 1 / (1 + k) = 1 / 3
k = 2
prob_theoretical = 1 / (1 + k)


print(f"Theoretical probability: {prob_theoretical:.6f}")

