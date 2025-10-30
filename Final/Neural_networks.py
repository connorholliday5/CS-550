import numpy as np

# XOR data
X = np.array([[0,0],[0,1],[1,0],[1,1]], float)
y = np.array([[0],[1],[1],[0]], float)

# Tiny NN: 2 -> 4 -> 1
np.random.seed(0)
W1 = np.random.randn(2,4)*0.5; b1 = np.zeros((1,4))
W2 = np.random.randn(4,1)*0.5; b2 = np.zeros((1,1))

def relu(z):  return np.maximum(0,z)
def drelu(z): return (z>0).astype(float)
def sigmoid(z): return 1/(1+np.exp(-z))

lr, epochs = 0.1, 8000
for _ in range(epochs):
    z1 = X @ W1 + b1; a1 = relu(z1)
    z2 = a1 @ W2 + b2; yhat = sigmoid(z2)
    dz2 = (yhat - y)                 # BCE + sigmoid combo
    dW2 = a1.T @ dz2 / len(X); db2 = dz2.mean(0, keepdims=True)
    da1 = dz2 @ W2.T; dz1 = da1 * drelu(z1)
    dW1 = X.T @ dz1 / len(X); db1 = dz1.mean(0, keepdims=True)
    W2 -= lr*dW2; b2 -= lr*db2; W1 -= lr*dW1; b1 -= lr*db1

print("Preds:", (yhat>=0.5).astype(int).ravel())
