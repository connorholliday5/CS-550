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

# Secant method iterations 
def secant_iteration_safe(f, x0, x1, n=3, eps=1e-10):
    xs = [x0, x1]
    for _ in range(n):
        f_x0, f_x1 = f(xs[-2]), f(xs[-1])
        denom = f_x1 - f_x0
        if abs(denom) < eps:  # Avoid division by zero
            denom = eps
        x_new = xs[-1] - f_x1 * (xs[-1] - xs[-2]) / denom
        xs.append(x_new)
    return xs

# X-axis ranges
x_vals_range = {
    "default": np.linspace(-3, 3, 400),
    "positive": np.linspace(0.01, 3, 400)  # for sqrt and log
}

# Plot each function
for key, f in functions.items():
    if key in ["c", "f"]:
        x_vals = x_vals_range["positive"]
    else:
        x_vals = x_vals_range["default"]

    # Initial guesses 
    x0, x1 = 3, 2.5
    xs = secant_iteration_safe(f, x0, x1)

    # Plot function
    plt.figure()
    plt.plot(x_vals, f(x_vals), 'g', label='f(x)')

    # Colors for secant lines
    colors = ['r', 'b', 'g']

    for i in range(3):
        slope = (f(xs[i+1]) - f(xs[i])) / (xs[i+1] - xs[i] + 1e-10)
        intercept = f(xs[i]) - slope * xs[i]
        secant_line = slope * x_vals + intercept
        plt.plot(x_vals, secant_line, colors[i], linestyle='--', label=f'Secant {i+1}')

    plt.title(f"Secant Method for function {key}")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)

plt.show()
