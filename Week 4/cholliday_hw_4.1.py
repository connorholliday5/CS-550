import numpy as np
import matplotlib.pyplot as plt

# Generate the unit circle
theta = np.linspace(0, 2 * np.pi, 500)
circle = np.array([np.cos(theta), np.sin(theta)])

# Define transformation matrices
M1 = np.array([[1.5, 0], [0, 1]])           # Expand x by 1.5
M2 = np.array([[1, 0], [0, 0.75]])          # Contract y by 0.75
M3 = np.array([[1, 2], [0, 1]])             # Shear x by 2
M4 = np.array([[1, 0], [1.25, 1]])          # Shear y by 1.25
M5 = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],  # Rotate CCW by π/4
               [np.sin(np.pi/4), np.cos(np.pi/4)]])
M6 = np.array([[np.cos(-np.pi/6), -np.sin(-np.pi/6)], # Rotate CW by π/6
               [np.sin(-np.pi/6), np.cos(-np.pi/6)]])

matrices = [M1, M2, M3, M4, M5, M6]
titles = ["Expand x by 1.5", "Contract y by 0.75", "Shear x by 2", 
          "Shear y by 1.25", "Rotate CCW π/4", "Rotate CW π/6"]

# Plot setup
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Original area of unit circle
original_area = np.pi

# Apply transformations and plot
for ax, M, title in zip(axes.flat, matrices, titles):
    transformed_circle = M @ circle
    ax.plot(transformed_circle[0], transformed_circle[1], label='Transformed Circle')
    ax.set_title(title)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    # Compute and display the area change by determinant
    area = abs(np.linalg.det(M)) * original_area
    ax.text(0.05, 0.9, f"Area ≈ {area:.2f}", transform=ax.transAxes)

plt.tight_layout()
plt.show()
