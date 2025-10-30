import numpy as np

# Define all 2x2 transformation matrices same as 3,1 
M1 = np.array([[1.5, 0], [0, 1]])                  # Expand x by 1.5
M2 = np.array([[1, 0], [0, 0.75]])                # Contract y by 0.75
M3 = np.array([[1, 2], [0, 1]])                   # Shear along x by 2
M4 = np.array([[1, 0], [1.25, 1]])                # Shear along y by 1.25
M5 = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
               [np.sin(np.pi/4), np.cos(np.pi/4)]])  # Rotate CCW π/4
M6 = np.array([[np.cos(-np.pi/6), -np.sin(-np.pi/6)],
               [np.sin(-np.pi/6), np.cos(-np.pi/6)]])  # Rotate CW π/6

# Store matrices
matrices = {"M1": M1, "M2": M2, "M3": M3, "M4": M4, "M5": M5, "M6": M6}

# Manual inverse function using 2x2 formula
def manual_inverse(M):
    a, b = M[0, 0], M[0, 1]
    c, d = M[1, 0], M[1, 1]
    det = a * d - b * c
    if det == 0:
        return None
    inv = (1 / det) * np.array([[d, -b], [-c, a]])
    return inv

# display results
for name, M in matrices.items():
    print(f"\n{name}:")
    print("Original Matrix:")
    print(np.round(M, 4))
    
    inv_manual = manual_inverse(M)
    inv_numpy = np.linalg.inv(M)

    print("Manual Inverse:")
    print(np.round(inv_manual, 4))

    print("Numpy Inverse:")
    print(np.round(inv_numpy, 4))
