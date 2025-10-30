import numpy as np
import matplotlib.pyplot as plt

# Define transformation matrices
M1 = np.array([[1.5, 0], [0, 1]])           # Expand x by 1.5
M2 = np.array([[1, 0], [0, 0.75]])          # Contract y by 0.75
M3 = np.array([[1, 2], [0, 1]])             # Shear x by 2
M4 = np.array([[1, 0], [1.25, 1]])          # Shear y by 1.25
M5 = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
               [np.sin(np.pi/4), np.cos(np.pi/4)]])   # Rotate π/4
M6 = np.array([[np.cos(-np.pi/6), -np.sin(-np.pi/6)],
               [np.sin(-np.pi/6), np.cos(-np.pi/6)]]) # Rotate -π/6

# Combined transformations
T_a = np.linalg.matrix_power(M1, 2) @ np.linalg.matrix_power(M3, 3) @ M5
T_b = np.linalg.inv(M2) @ np.linalg.matrix_power(np.linalg.inv(M4), 2) @ M6

# Create unit circle
theta = np.linspace(0, 2 * np.pi, 500)
circle = np.array([np.cos(theta), np.sin(theta)])
original_area = np.pi

# Apply transformations
circle_a = T_a @ circle
circle_b = T_b @ circle
area_a = abs(np.linalg.det(T_a)) * original_area
area_b = abs(np.linalg.det(T_b)) * original_area

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].plot(circle_a[0], circle_a[1], label='Transformed C (a)')
axes[0].set_title(f"(M1^2)(M3^3)M5\nArea ≈ {area_a:.2f}")
axes[0].set_aspect('equal')
axes[0].grid(True)
axes[0].set_xlim(-10, 10)
axes[0].set_ylim(-10, 10)

axes[1].plot(circle_b[0], circle_b[1], label='Transformed C (b)', color='orange')
axes[1].set_title(f"(M2^-1)(M4^-2)M6\nArea ≈ {area_b:.2f}")
axes[1].set_aspect('equal')
axes[1].grid(True)
axes[1].set_xlim(-10, 10)
axes[1].set_ylim(-10, 10)

plt.tight_layout()
plt.show()
