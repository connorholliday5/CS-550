import numpy as np

#  matrices A and B
A = np.array([[1, 2],
              [3, 4]], dtype=float)

B = np.array([[5, 9],
              [2, 5]], dtype=float)

# Identity matrix
I = np.eye(2)

# Function to compute log(M) ≈ (M - I) - 1/2*(M - I)^2 + 1/3*(M - I)^3
def matrix_log_approx(M):
    M1 = M - I
    M2 = M1 @ M1
    M3 = M1 @ M1 @ M1
    return M1 - 0.5 * M2 + (1/3) * M3

# Compute inverses of A and B
A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)

# Compute approximated logarithms
log_A = matrix_log_approx(A)
log_A_inv = matrix_log_approx(A_inv)
log_B = matrix_log_approx(B)
log_B_inv = matrix_log_approx(B_inv)

# Display results
def print_matrix(name, mat):
    print(f"\n{name}:")
    print(np.round(mat, 4))

print_matrix("log(A)", log_A)
print_matrix("log(A^-1)", log_A_inv)
print_matrix("log(B)", log_B)
print_matrix("log(B^-1)", log_B_inv)
