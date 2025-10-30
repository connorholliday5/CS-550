import numpy as np
from sklearn.linear_model import LogisticRegression

# Training data
X = np.array([[0,0],[1,0],[0,1],[1,1]])
y = np.array([0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

print("Predicted Probability:", model.predict_proba([[0.5, 0.5]]))
print("Predicted Class:", model.predict([[0.5, 0.5]]))
