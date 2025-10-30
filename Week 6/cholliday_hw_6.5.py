import sympy as sp

# Define the symmetric matrix A for Q(x, y, z)
A = sp.Matrix([
    [2, 10, -2],  
    [10, 5, 8],   
    [-2, 8, 11]
])

#  matrix
print("a) Symmetric matrix representation A:")
sp.pprint(A)

# compute eigenvalues
eigenvalues = A.eigenvals()
print("\nb) Eigenvalues of A:")
for val, mult in eigenvalues.items():
    print(f"  λ = {val}, multiplicity = {mult}")

# determine positive-definiteness
is_positive_definite = all(val > 0 for val in eigenvalues)
print("\nc) Is Q(x, y, z) positive-definite?")
print("  Yes" if is_positive_definite else "  No")
