import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(-4,4,1000)
x_val = 1

#define functions and derivatives 

functions = [
    ("f(x) = 2", lambda x: 2*np.ones_like(x), lambda x: np.zeros_like(x)),
    ("f(x) = x + 1", lambda x: x + 1, lambda x: np.ones_like(x)),
    ("f(x) = 2x² + x", lambda x: 2*x**2 + x, lambda x: 4*x + 1),
    ("f(x) = x³ + 3", lambda x: x**3 + 3, lambda x: 3*x**2),
    ("f(x) = 2√x", lambda x: 2*np.sqrt(x), lambda x: 1/np.sqrt(x)),
    ("f(x) = e^(x+1)", lambda x: np.exp(x + 1), lambda x: np.exp(x)),
    ("f(x) = 3^x", lambda x: 3**x, lambda x: np.log(3) * 3**x),
    ("f(x) = log(x) + 1", lambda x: np.log(x) + 1, lambda x: 1/x),
    ("f(x) = sin(x + π/6)", lambda x: np.sin(x + np.pi/6), lambda x: np.cos(x)),
    ("f(x) = cos(x + π/6)", lambda x: np.cos(x + np.pi/6), lambda x: -np.sin(x)),
]

# subplots
fig,axs = plt.subplots(5,2, figsize=(15,20))
axs = axs.ravel()

for i, (title, f, df) in enumerate(functions):
    ax = axs[i]

     # Handle domain issues (e.g., sqrt and log)
    if "√x" in title or "log" in title:
        x_plot = x[x > 0]
    else:
        x_plot = x

    fx = f(x_plot)
    dfx = df(x_plot)

    # Plot f(x) and f'(x)
    ax.plot(x_plot, fx, label="$f(x)$", color='green')
    ax.plot(x_plot, dfx, label="$f'(x)$", color='red')

    # Plot f(1) and f'(1) if in domain
    if x_val >= x_plot[0] and x_val <= x_plot[-1]:
        ax.plot(x_val, f(x_val), 'ko')   
        ax.plot(x_val, df(x_val), 'ko')   
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title(title)
    ax.legend(frameon=False)
    ax.grid(True)

plt.tight_layout()
plt.show()