import sympy as sp

# Define matrix A and lambda symbol
λ = sp.symbols('λ')
A = sp.Matrix([[1, 2], [3, 4]])

# a) Characteristic polynomial
char_poly = A.charpoly(λ)
print("a) Characteristic Polynomial:")
print(char_poly.as_expr())  # λ^2 - 5λ - 2

# b) Eigenvalues
print("\nb) Eigenvalues:")
eigenvals = A.eigenvals()
for val, mult in eigenvals.items():
    print(f"λ = {val}, multiplicity = {mult}")

# c) Eigenvectors
print("\nc) Eigenvectors:")
eigenvects = A.eigenvects()
for val, mult, vects in eigenvects:
    print(f"λ = {val}")
    for v in vects:
        sp.pprint(v)

# d) Verify Cayley-Hamilton: P(A) = A^2 - 5A - 2I
I = sp.eye(2)
P_A = A**2 - 5*A - 2*I
print("\nd) P(A):")
sp.pprint(P_A)

# Check if it's zero matrix
print("\nCayley-Hamilton Verified:", P_A == sp.zeros(2))
