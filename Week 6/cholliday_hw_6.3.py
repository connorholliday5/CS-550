import numpy as np
import matplotlib.pyplot as plt

# Define functions
functions = {
    "a": (lambda x: x**2 - 5),
    "b": (lambda x: x**3 - 5),
    "c": (lambda x: np.sqrt(x) - 1.5),
    "d": (lambda x: np.exp(x) - 2),
    "e": (lambda x: 2*x - 0.5),
    "f": (lambda x: np.log(x) - 1),
    "g": (lambda x: np.sin(x) - 0.5),
    "h": (lambda x: np.cos(x) - 0.5)
}

# Bisection method iterations
def bisection_iterations(f, a, b, n=3):
    xs = []
    for _ in range(n):
        mid = (a + b) / 2
        xs.append(mid)
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return xs

# X-axis ranges
x_vals_range = {
    "default": np.linspace(-3, 3, 400),
    "positive": np.linspace(0.01, 3, 400)  
}

# Plot each function
for key, f in functions.items():
    if key in ["c", "f"]:
        x_vals = x_vals_range["positive"]
        a, b = 0.01, 3  
    else:
        x_vals = x_vals_range["default"]
        a, b = -3, 3

    xs = bisection_iterations(f, a, b)

    plt.figure()
    plt.plot(x_vals, f(x_vals), 'g', label='f(x)')
    
    # Scatter points for x1, x2, x3
    colors = ['r', 'b', 'g']
    for i, x_point in enumerate(xs):
        plt.scatter(x_point, f(x_point), color=colors[i], s=100, label=f"x{i+1}")

    plt.title(f"Bisection Method for function {key}")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)

plt.show()
