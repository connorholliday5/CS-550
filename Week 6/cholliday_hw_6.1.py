import numpy as np
import matplotlib.pyplot as plt

# Define functions 
functions = {
    "a": (lambda x: x**2 - 5, lambda x: 2*x),
    "b": (lambda x: x**3 - 5, lambda x: 3*x**2),
    "c": (lambda x: np.sqrt(x) - 1.5, lambda x: 1/(2*np.sqrt(x))),
    "d": (lambda x: np.exp(x) - 2, lambda x: np.exp(x)),
    "e": (lambda x: 2*x - 0.5, lambda x: 2*np.ones_like(x)),
    "f": (lambda x: np.log(x) - 1, lambda x: 1/x),
    "g": (lambda x: np.sin(x) - 0.5, lambda x: np.cos(x)),
    "h": (lambda x: np.cos(x) - 0.5, lambda x: -np.sin(x))
}

# Newton's method iterations
def newton_iteration(f, f_prime, x0, n=3):
    xs = [x0]
    for _ in range(n):
        x0 = x0 - f(x0) / f_prime(x0)
        xs.append(x0)
    return xs

# Range settings
x_vals_range = {
    "default": np.linspace(-3, 3, 400),
    "positive": np.linspace(0.01, 3, 400)  #
}

# Plot each function and tangent lines
for key, (f, f_prime) in functions.items():
    if key in ["c", "f"]:
        x_vals = x_vals_range["positive"]
    else:
        x_vals = x_vals_range["default"]
    
    x0 = 3
    xs = newton_iteration(f, f_prime, x0)
    
    plt.figure()
    plt.plot(x_vals, f(x_vals), 'g', label='f(x)')
    
    colors = ['r', 'b', 'g']
    for i in range(3):
        slope = f_prime(xs[i])
        intercept = f(xs[i]) - slope * xs[i]
        tangent_line = slope * x_vals + intercept
        plt.plot(x_vals, tangent_line, colors[i], linestyle='--', label=f'Tangent {i+1}')
    
    plt.title(f"Newton's Method for function {key}")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)

plt.show()
