import numpy as np

#  A(0,0), B(0,1), C(1,1), D(1,0)
square = np.array([[0, 0],   # A
                   [0, 1],   # B
                   [1, 1],   # C
                   [1, 0]])  # D

# Transformation matrices
M1 = np.array([[1.5, 0], [0, 1]])             # Expand x by 1.5
M2 = np.array([[1, 0], [0, 0.75]])            # Contract y by 0.75
M3 = np.array([[1, 2], [0, 1]])               # Shear along x by 2
M4 = np.array([[1, 0], [1.25, 1]])            # Shear along y by 1.25
M5 = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)], 
               [np.sin(np.pi/4), np.cos(np.pi/4)]])  # Rotate CCW π/4
M6 = np.array([[np.cos(-np.pi/6), -np.sin(-np.pi/6)], 
               [np.sin(-np.pi/6), np.cos(-np.pi/6)]])  # Rotate CW π/6

transformations = {
    "M1": M1,
    "M2": M2,
    "M3": M3,
    "M4": M4,
    "M5": M5,
    "M6": M6
}

labels = ['A', 'B', 'C', 'D']

# Apply transformations and print new vertices
for name, matrix in transformations.items():
    print(f"\n{name} - Transformed Vertices:")
    transformed = square @ matrix.T
    for label, coord in zip(labels, transformed):
        print(f"{label}': ({coord[0]:.3f}, {coord[1]:.3f})")
