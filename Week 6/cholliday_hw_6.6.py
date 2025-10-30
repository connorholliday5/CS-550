import sympy as sp

# Define symbol
x = sp.symbols('x', real=True)

# Define functions
f = sp.exp(-(x + 1)**2)
g = sp.log(-(x + 1)**2)
h = (x - 2)**4 + (x - 1)**2

# 1. f(x) minimum
# For f(x) = exp(-(x+1)^2), minimum over reals is limit as |x| -> infinity
f_min_value = 0
print("f(x) = exp(-(x+1)^2)")
print(f"  Minimum value (over reals): {f_min_value} (approached as |x| → ∞)")
print()

# 2. g(x) domain and minimum
print("g(x) = log(-(x+1)^2)")
# Find domain in reals: solve -(x+1)^2 > 0
g_domain = sp.solve(sp.StrictGreaterThan(-(x+1)**2, 0), x)
if not g_domain:
    print("  No real domain — function undefined for real x.")
else:
    print(f"  Domain: {g_domain}")
print()

# 3. h(x) minimum
print("h(x) = (x-2)^4 + (x-1)^2")
# First derivative
h_prime = sp.diff(h, x)
# Solve h'(x) = 0
critical_points = sp.solve(h_prime, x)
# Filter only real points
critical_points_real = [cp.evalf() for cp in critical_points if cp.is_real]
# Evaluate h(x) at each real critical point
h_values_real = [h.subs(x, cp).evalf() for cp in critical_points_real]
# Find the minimum value
h_min_value = min(h_values_real)
# Corresponding x value(s)
h_min_points = [critical_points_real[i] for i, val in enumerate(h_values_real) if val == h_min_value]

print(f"  Critical points (real): {critical_points_real}")
print(f"  Minimum value: {h_min_value} at x = {h_min_points}")
