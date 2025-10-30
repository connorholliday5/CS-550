#  X = {0, 1, ..., 99}
X_values = list(range(100))
total = len(X_values) 

# (a) P(X >= 25)
count_a = sum(1 for x in X_values if x >= 25)
P_a = count_a / total

# (b) P(2.5 < X < 12.5)
count_b = sum(1 for x in X_values if 2.5 < x < 12.5)
P_b = count_b / total

# (c) P(8 < X <= 10 or 30 < X <= 32)
count_c = sum(1 for x in X_values if (8 < x <= 10) or (30 < x <= 32))
P_c = count_c / total

# (d) P(50 < X <= 70 or 60 < X <= 80)
count_d = sum(1 for x in X_values if (50 < x <= 70) or (60 < x <= 80))
P_d = count_d / total

# Print results
print(f"(a) P(X >= 25) = {P_a:.2f}")
print(f"(b) P(2.5 < X < 12.5) = {P_b:.2f}")
print(f"(c) P(8 < X <= 10 or 30 < X <= 32) = {P_c:.2f}")
print(f"(d) P(50 < X <= 70 or 60 < X <= 80) = {P_d:.2f}")
