import numpy as np

# Define matrices
A = np.array([[1, 2],
              [3, 4]], dtype=float)

B = np.array([[5, 9],
              [2, 5]], dtype=float)

C = np.array([[2, 1, 0],
              [3, 6, 1],
              [5, 7, 1]], dtype=float)

def gauss_jordan_inverse_pivot(M):
    n = M.shape[0]
    A = np.hstack([M.astype(float), np.eye(n)])
    
    for i in range(n):
        # pivoting
        max_row = np.argmax(np.abs(A[i:, i])) + i
        if A[max_row, i] == 0:
            return None  
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]  # Swap rows

        # Normalize pivot row
        A[i] = A[i] / A[i, i]

        # Eliminate other rows
        for j in range(n):
            if j != i:
                A[j] = A[j] - A[j, i] * A[i]
    
    return A[:, n:]

# Function to attempt inversion and handle singular cases
def attempt_inverse(name, M):
    print(f"\nMatrix {name}:")
    print(np.round(M, 3))

    det = np.linalg.det(M)
    print(f"Determinant of {name}: {det:.4f}")

    if np.isclose(det, 0):
        print(f"Matrix {name} is singular and not invertible.")
        return None
    else:
        inv = gauss_jordan_inverse_pivot(M)
        print(f"Inverse of {name} (Gauss-Jordan with pivoting):")
        print(np.round(inv, 4))
        return inv

# Apply to A, B, C
inv_A = attempt_inverse("A", A)
inv_B = attempt_inverse("B", B)
inv_C = attempt_inverse("C", C)
