import numpy as np
import pandas as pd
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Step size and evaluation point
dx = 0.2
x_val = 1.0

# Functions and exact derivatives
functions = [
    ("f(x) = 2", lambda x: 2*np.ones_like(x), lambda x: 0),
    ("f(x) = x + 1", lambda x: x + 1, lambda x: 1),
    ("f(x) = 2x² + x", lambda x: 2*x**2 + x, lambda x: 4*x + 1),
    ("f(x) = x³ + 3", lambda x: x**3 + 3, lambda x: 3*x**2),
    ("f(x) = 2√x", lambda x: 2*np.sqrt(x), lambda x: 1/np.sqrt(x)),
    ("f(x) = e^(x+1)", lambda x: np.exp(x + 1), lambda x: np.exp(x)),
    ("f(x) = 3^x", lambda x: 3**x, lambda x: np.log(3) * 3**x),
    ("f(x) = log(x) + 1", lambda x: np.log(x) + 1, lambda x: 1/x),
    ("f(x) = sin(x + π/6)", lambda x: np.sin(x + np.pi/6), lambda x: np.cos(x)),
    ("f(x) = cos(x + π/6)", lambda x: np.cos(x + np.pi/6), lambda x: -np.sin(x)),
]

print(f"{'Function':25} {'Forward':>10} {'Backward':>10} {'Central':>10} {'Exact':>10}")

# Loop over functions
for name, f, df in functions:
    f_x = f(x_val)
    f_x_plus = f(x_val + dx)
    f_x_minus = f(x_val - dx)

    forward = (f_x_plus - f_x) / dx
    backward = (f_x - f_x_minus) / dx
    central = (f_x_plus - f_x_minus) / (2 * dx)
    exact = df(x_val)

    values = [forward, backward, central]
    errors = [abs(forward - exact), abs(backward - exact), abs(central - exact)]
    min_error = min(errors)
    max_error = max(errors)

    def highlight(val, err):
        if np.isclose(err, min_error, atol=1e-6):
            return Fore.GREEN + f"{val:10.4f}" + Style.RESET_ALL
        elif np.isclose(err, max_error, atol=1e-6):
            return Fore.RED + f"{val:10.4f}" + Style.RESET_ALL
        else:
            return f"{val:10.4f}"

    f_str = highlight(forward, errors[0])
    b_str = highlight(backward, errors[1])
    c_str = highlight(central, errors[2])
    e_str = f"{exact:10.4f}"

    print(f"{name:25} {f_str} {b_str} {c_str} {e_str}")
