import numpy as np
import matplotlib.pyplot as plt

# Function for majority voting accuracy for N = 3
def majority_accuracy_N3(p):
    return 3 * p**2 - 2 * p**3

# Generate accuracy values for p in [0.5, 1]
p_values = np.linspace(0.5, 1, 200)
ensemble_accuracy = majority_accuracy_N3(p_values)

# Plot the results
plt.figure(figsize=(8,5))
plt.plot(p_values, ensemble_accuracy, label="Majority Vote Accuracy (N=3)", linewidth=2)
plt.plot(p_values, p_values, '--', label="Single Classifier Accuracy", linewidth=2)
plt.xlabel("Single Classifier Accuracy (p)")
plt.ylabel("Accuracy")
plt.title("Majority Voting Accuracy for N=3 Classifiers")
plt.legend()
plt.grid(True)
plt.show()
