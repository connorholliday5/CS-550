import random

# Define possible X values
X_values = [-12, -10, -8, -6, -4, -2, 3, 5, 7, 9, 11]
counts = [1, 3, 5, 5, 3, 1, 2, 4, 6, 4, 2] 
total_outcomes = 36

probabilities = [c / total_outcomes for c in counts]

#distribution table
print("Probability Distribution Table:")
print(f"{'X':>4} {'P(X)':>10}")
for x, p in zip(X_values, probabilities):
    print(f"{x:>4} {p:>10.4f}")

#Expected value
expected_value = sum(x * p for x, p in zip(X_values, probabilities))
print(f"\nExpected Value E[X] = {expected_value:.4f}")

