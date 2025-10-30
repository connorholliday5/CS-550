import numpy as np
from scipy.integrate import quad, simpson
import matplotlib.pyplot as plt

# Define x range for trapezoid and Simpson
x = np.linspace(1, 5, 1000)

# List of functions: (label, lambda)
functions = [
    ("f(x) = 2", lambda x: 2 * np.ones_like(x)),
    ("f(x) = x + 1", lambda x: x + 1),
    ("f(x) = 2x² + x", lambda x: 2 * x**2 + x),
    ("f(x) = x³ + 3", lambda x: x**3 + 3),
    ("f(x) = 2√x", lambda x: 2 * np.sqrt(x)),
    ("f(x) = e^(x+1)", lambda x: np.exp(x + 1)),
    ("f(x) = 3^x", lambda x: 3**x),
    ("f(x) = log(x) + 1", lambda x: np.log(x) + 1),
    ("f(x) = sin(x + π/6)", lambda x: np.sin(x + np.pi/6)),
    ("f(x) = cos(x + π/6)", lambda x: np.cos(x + np.pi/6)),
]


# Header
print(f"{'Function':30} {'Quad':>10} {'Trapezoid':>12} {'Simpson':>10}")

# Integration results
for name, f in functions:
    y = f(x)
    
    # 1. Fixed quadrature
    quad_val, _ = quad(f, 1, 5)
    
    # 2. Trapezoid rule
    trapezoid_val = np.trapezoid(y, x)
    
    # 3. Simpson's rule
    simp_val = simpson(y, x)
    
    print(f"{name:30} {quad_val:10.4f} {trapezoid_val:12.4f} {simp_val:10.4f}")
