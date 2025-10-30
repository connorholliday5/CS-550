import numpy as np

# Given values
EX4 = 2
EY2 = 1
EX2 = 1
EY = 0

# Var(X^2 Y) = E[X^4] * E[Y^2] - (E[X^2] * E[Y])^2
var_theoretical = EX4 * EY2 - (EX2 * EY) ** 2

print(f"Theoretical Var(X^2 Y) = {var_theoretical}")

