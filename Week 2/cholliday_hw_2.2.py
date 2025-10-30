from sympy import symbols, diff, sqrt, exp, log, sin, cos, simplify, pprint, init_printing

init_printing()  # Pretty print output
x, n = symbols('x n')

functions = [
    ("f(x) = 2", 2),
    ("f(x) = x + 1", x + 1),
    ("f(x) = 2x^2 + x", 2*x**2 + x),
    ("f(x) = x^n + n (n=3)", x**3 + 3),  # setting n=3 directly
    ("f(x) = 2√x", 2*sqrt(x)),
    ("f(x) = e^(x+1)", exp(x + 1)),
    ("f(x) = 3^x", 3**x),
    ("f(x) = log(x) + 1", log(x) + 1),
    ("f(x) = sin(x + π/6)", sin(x + 3.14159/6)),
    ("f(x) = cos(x + π/6)", cos(x + 3.14159/6))
]

# Print function and derivative for each
for title, f_expr in functions:
    print(f" {title} ")
    derivative = diff(f_expr, x)
    print("f(x):")
    pprint(f_expr)
    print("f'(x):")
    pprint(simplify(derivative))
    print("\n")
