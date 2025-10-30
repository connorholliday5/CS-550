import sympy as sp

# Define the symbol
x = sp.symbols('x', real=True)

# Define each function equation f(x)=0
functions = {
    "a": x**2 - 5,
    "b": x**3 - 5,
    "c": sp.sqrt(x) - 1.5,
    "d": sp.exp(x) - 2,
    "e": 2*x - 0.5,
    "f": sp.log(x) - 1,
    "g": sp.sin(x) - 0.5,
    "h": sp.cos(x) - 0.5
}

# Solve each equation
for key, expr in functions.items():
    sol = sp.solveset(expr, x, domain=sp.S.Reals)
    print(f"Function {key}, solveset gives:")
    print(sol)
