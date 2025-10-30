import numpy as np


# System 1:
# 2x + 3y = 8
# 2x - y = 0
A1 = np.array([[2, 3],
               [2, -1]], dtype=float)
b1 = np.array([8, 0], dtype=float)

# System 2:
# x + 2y = -2
# 2x + y = 2
A2 = np.array([[1, 2],
               [2, 1]], dtype=float)
b2 = np.array([-2, 2], dtype=float)

# System 3:
# 2x + 3y + 4z = 4
# x - y + z = 1
# 2x - y + z = 1
A3 = np.array([[2, 3, 4],
               [1, -1, 1],
               [2, -1, 1]], dtype=float)
b3 = np.array([4, 1, 1], dtype=float)

#System 4: 
# x + y + z = 1
# 2x + y + z = 2
# x + 2y + 2z = 1

A4 = np.array([[1,1,1],
                [2,1,1],
                [1,2,2]], dtype=float)
b4 = np.array([1, 2, 1], dtype=float)
# Function to solve using numpy or analyze system rank
def solve_linear_system(A, b):
    rank_A = np.linalg.matrix_rank(A)
    rank_Ab = np.linalg.matrix_rank(np.hstack([A, b.reshape(-1, 1)]))
    if rank_A != rank_Ab:
        return "No solution"
    elif rank_A < A.shape[1]:
        return "Infinitely many solutions"
    else:
        return np.linalg.solve(A, b)

# Solve each system
sol1 = solve_linear_system(A1, b1)
sol2 = solve_linear_system(A2, b2)
sol3 = solve_linear_system(A3, b3)
sol4 = solve_linear_system(A4, b4)

# Display results
def display_solution(name, solution):
    print(f"\n{name}:")
    if isinstance(solution, str):
        print(solution)
    else:
        for i, val in enumerate(solution):
            print(f"{chr(120 + i)} = {val:.4f}")  # chr(120) = 'x'

display_solution("System 1", sol1)
display_solution("System 2", sol2)
display_solution("System 3", sol3)
display_solution("System 4", sol4)
