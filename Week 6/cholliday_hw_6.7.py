import sympy as sp

# Define variables
x, y, lam = sp.symbols('x y lam', real=True)

# Define function and constraint
f = x**2 + 2*y**2
g = x - 2*y + 1  # constraint g(x, y) = 0

# a) Lagrangian
L = f + lam * g
print("a) Lagrangian L:")
sp.pprint(L)
print()

# b) Gradient of L
grad_L = [sp.diff(L, var) for var in (x, y, lam)]
print("b) Gradient ∇L:")
for var, dL in zip((x, y, lam), grad_L):
    print(f"∂L/∂{var} =", dL)
print()

# c) Equations for ∇L = 0
eqs = [sp.Eq(dL, 0) for dL in grad_L]
print("c) Equations for ∇L = 0:")
for eq in eqs:
    sp.pprint(eq)
print()

# d) Solve the system
solution = sp.solve(eqs, (x, y, lam), dict=True)
print("d) Solution (x, y, λ):")
print(solution)

# Minimum value of f(x, y)
if solution:
    sol_point = solution[0]
    f_min = f.subs(sol_point)
    print(f"\nMinimum value of f(x, y): {f_min}")
