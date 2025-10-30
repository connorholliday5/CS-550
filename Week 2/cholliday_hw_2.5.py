from sympy import symbols, integrate, sqrt, exp, log, sin, cos, pi, pprint, N

# Define symbolic variable
x = symbols('x')

# List of functions with titles
functions = [
    ("f(x) = 2", 2),
    ("f(x) = x + 1", x + 1),
    ("f(x) = 2x² + x", 2*x**2 + x),
    ("f(x) = x³ + 3", x**3 + 3),
    ("f(x) = 2√x", 2*sqrt(x)),
    ("f(x) = e^(x+1)", exp(x + 1)),
    ("f(x) = 3^x", 3**x),
    ("f(x) = log(x) + 1", log(x) + 1),
    ("f(x) = sin(x + π/6)", sin(x + pi/6)),
    ("f(x) = cos(x + π/6)", cos(x + pi/6))
]

# Compute and display definite integrals from x = 1 to 5
for title, f_expr in functions:
    definite_integral = integrate(f_expr, (x, 1, 5))
    numeric_value = N(definite_integral)  # Evaluate to float
    print(f"{title}")
    print("∫ from 1 to 5 =", numeric_value)

