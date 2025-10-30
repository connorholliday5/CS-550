import numpy as np
import matplotlib.pyplot as plt

# x range and step size
x = np.linspace(1, 5, 500)
dx = x[1] - x[0]

# Define all 10 functions
functions = [
    ("f(x) = 2", lambda x: 2*np.ones_like(x)),
    ("f(x) = x + 1", lambda x: x + 1),
    ("f(x) = 2x² + x", lambda x: 2*x**2 + x),
    ("f(x) = x³ + 3", lambda x: x**3 + 3),
    ("f(x) = 2√x", lambda x: 2*np.sqrt(x)),
    ("f(x) = e^(x+1)", lambda x: np.exp(x + 1)),
    ("f(x) = 3^x", lambda x: 3**x),
    ("f(x) = log(x) + 1", lambda x: np.log(x) + 1),
    ("f(x) = sin(x + π/6)", lambda x: np.sin(x + np.pi/6)),
    ("f(x) = cos(x + π/6)", lambda x: np.cos(x + np.pi/6)),
]

# Set up subplots
fig, axs = plt.subplots(5, 2, figsize=(15, 20))
axs = axs.ravel()

for i, (title, func) in enumerate(functions):
    ax = axs[i]
    
    # Evaluate function
    y = func(x)
    
    # Plot the function f(x) in green
    ax.plot(x, y, label='f(x)', color='green')
    
    # Draw Riemann rectangles (left-endpoint)
    for j in range(len(x) - 1):
        ax.add_patch(plt.Rectangle((x[j], 0), dx, y[j], color='red', alpha=0.2))
    
    # Mark f(1) in black
    ax.plot(1, func(1), 'ko', label='f(1)')
    
    # Add plot formatting
    ax.set_title(title)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend(frameon=False)
    ax.grid(True)

plt.tight_layout()
plt.show()
