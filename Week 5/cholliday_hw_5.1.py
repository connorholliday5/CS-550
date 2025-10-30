# Given values
pi_true = 3.1315
tol = 1e-5

#  N = 100
N = 100

# a) n = 10
n_a = 10
pi_a = 4 * n_a / N

# b) n = 20
n_b = 20
pi_b = 4 * n_b / N

# c) Find smallest N where |4n/N - pi_true| < tol
min_N = None
min_n = None

for N_test in range(1, 10**6):
    for n_test in range(N_test + 1):
        if abs(4 * n_test / N_test - pi_true) < tol:
            min_N = N_test
            min_n = n_test
            break
    if min_N is not None:
        break

# Fresults
print(f"(a) For n = {n_a}, N = {N}, pi ≈ {pi_a}")
print(f"(b) For n = {n_b}, N = {N}, pi ≈ {pi_b}")

if min_N is not None:
    print(f"(c) Smallest N for error < {tol}: N = {min_N}, n = {min_n}, pi ≈ {4 * min_n / min_N}")
else:
    print("(c) No N found within search limit that satisfies the tolerance.")
