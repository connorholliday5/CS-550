import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define real-valued transformation matrices
matrices = {
    "M1: Expand x": np.array([[1.5, 0], [0, 1]]),
    "M2: Contract y": np.array([[1, 0], [0, 0.75]]),
    "M3: Shear x": np.array([[1, 2], [0, 1]]),
    "M4: Shear y": np.array([[1, 0], [1.25, 1]]),
    "M5: Rotate π/4": np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
                                [np.sin(np.pi/4), np.cos(np.pi/4)]]),
    "M6: Rotate -π/6": np.array([[np.cos(-np.pi/6), -np.sin(-np.pi/6)],
                                 [np.sin(-np.pi/6), np.cos(-np.pi/6)]])
}

# Symbol for symbolic computation
lam = sp.symbols('λ')

# Prepare plot
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

for ax, (name, M) in zip(axes.flat, matrices.items()):
    # Characteristic polynomial
    M_sym = sp.Matrix(M)
    char_poly = sp.simplify(M_sym.charpoly(lam).as_expr())
    
    # Eigenvalues and vectors
    eigvals, eigvecs = np.linalg.eig(M)
    
    ax.set_title(name)
    ax.axhline(0, color='gray', lw=0.5)
    ax.axvline(0, color='gray', lw=0.5)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.grid(True)

    # Plot only if eigenvalues are real
    if np.isreal(eigvals).all():
        for i in range(len(eigvals)):
            v = eigvecs[:, i].real
            ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue')
            ax.text(v[0], v[1], f"λ={eigvals[i].real:.2f}", color='red')
    else:
        ax.text(0, 0, "Complex eigenvalues", color='purple', ha='center')

plt.tight_layout()
plt.show()
