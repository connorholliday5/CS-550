# Python_ex.py 
import torch, torch.nn as nn, torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

device = "cuda" if torch.cuda.is_available() else "cpu"

# Data
tfm = transforms.Compose([transforms.ToTensor()])
train_ds = datasets.MNIST(root="data", train=True,  download=True, transform=tfm)
test_ds  = datasets.MNIST(root="data", train=False, download=True, transform=tfm)
train_loader = DataLoader(train_ds, batch_size=64, shuffle=True)
test_loader  = DataLoader(test_ds,  batch_size=256)

# Model
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool  = nn.MaxPool2d(2,2)
        self.fc1   = nn.Linear(64*14*14, 10)
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        return self.fc1(x)

model = CNN().to(device)
opt = torch.optim.Adam(model.parameters(), lr=1e-3)

# Train (3 quick epochs)
for epoch in range(3):
    model.train()
    for x,y in train_loader:
        x,y = x.to(device), y.to(device)
        logits = model(x)
        loss = F.cross_entropy(logits, y)
        opt.zero_grad(); loss.backward(); opt.step()

# Evaluate
model.eval(); correct = total = 0
with torch.no_grad():
    for x,y in test_loader:
        x,y = x.to(device), y.to(device)
        pred = model(x).argmax(dim=1)
        total += y.size(0); correct += (pred==y).sum().item()
print("Test accuracy:", correct/total)
