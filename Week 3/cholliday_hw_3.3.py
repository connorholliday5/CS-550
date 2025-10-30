import numpy as np
import matplotlib.pyplot as plt

# Define  square vertices
square = np.array([[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]]) 

# Define all transformation matrices same as 3.1
M1 = np.array([[1.5, 0], [0, 1]])
M2 = np.array([[1, 0], [0, 0.75]])
M3 = np.array([[1, 2], [0, 1]])
M4 = np.array([[1, 0], [1.25, 1]])
M5 = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
               [np.sin(np.pi/4),  np.cos(np.pi/4)]])
M6 = np.array([[np.cos(-np.pi/6), -np.sin(-np.pi/6)],
               [np.sin(-np.pi/6),  np.cos(-np.pi/6)]])

# Compute powers and inverses
M1_squared = np.linalg.matrix_power(M1, 2)
M3_cubed = np.linalg.matrix_power(M3, 3)
M2_inv = np.linalg.inv(M2)
M4_inv_squared = np.linalg.matrix_power(np.linalg.inv(M4), 2)

#transformations
T1 = M1_squared @ M3_cubed @ M5
T2 = M2_inv @ M4_inv_squared @ M6

# Apply transformations to square
square_T1 = square @ T1.T
square_T2 = square @ T2.T

# Plot original and transformed shapes
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].plot(square[:, 0], square[:, 1], 'b-', label='Original')
axs[0].plot(square_T1[:, 0], square_T1[:, 1], 'r--', label='(M1^2)(M3^3)M5')
axs[0].set_title('Transformation 1')
axs[0].axis('equal')
axs[0].grid(True)
axs[0].legend()

axs[1].plot(square[:, 0], square[:, 1], 'b-', label='Original')
axs[1].plot(square_T2[:, 0], square_T2[:, 1], 'r--', label='(M2^-1)(M4^-2)M6')
axs[1].set_title('Transformation 2')
axs[1].axis('equal')
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.show()

# Print new vertices
labels = ['A', 'B', 'C', 'D']
print("\nTransformed Vertices (T1 = (M1^2)(M3^3)M5):")
for label, coord in zip(labels, square_T1[:-1]):
    print(f"{label}': ({coord[0]:.3f}, {coord[1]:.3f})")

print("\nTransformed Vertices (T2 = (M2^-1)(M4^-2)M6):")
for label, coord in zip(labels, square_T2[:-1]):
    print(f"{label}': ({coord[0]:.3f}, {coord[1]:.3f})")
