"""
PyTorch 入门 Demo 3：手写一个多层神经网络做二分类
==================================================
任务：判断一个二维平面上的点是在「圆内」还是「圆外」。
你将看到 PyTorch 中标准的「自定义模型 + 训练 + 评估」写法。
"""

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

# ---------- 1. 造数据：圆内 label=1, 圆外 label=0 ----------
torch.manual_seed(0)
N = 1000
X = torch.randn(N, 2) * 2                         # 二维点
y = (X.pow(2).sum(dim=1) < 2.0).long()            # 在半径 sqrt(2) 圆内则为 1

# 划分训练集/测试集
train_ds = TensorDataset(X[:800], y[:800])
test_ds = TensorDataset(X[800:], y[800:])
train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
test_loader = DataLoader(test_ds, batch_size=32)

# ---------- 2. 自定义模型（继承 nn.Module 的标准写法） ----------
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 16),
            nn.ReLU(),
            nn.Linear(16, 16),
            nn.ReLU(),
            nn.Linear(16, 2),   # 输出 2 类的 logits
        )

    def forward(self, x):
        return self.net(x)

model = MLP()
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# ---------- 3. 训练 ----------
for epoch in range(20):
    model.train()
    total_loss = 0.0
    for xb, yb in train_loader:
        logits = model(xb)
        loss = loss_fn(logits, yb)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * xb.size(0)

    print(f"Epoch {epoch+1:2d} | train_loss={total_loss/len(train_ds):.4f}")

# ---------- 4. 评估 ----------
model.eval()
correct = 0
with torch.no_grad():           # 评估时不需要计算梯度，更快更省内存
    for xb, yb in test_loader:
        pred = model(xb).argmax(dim=1)
        correct += (pred == yb).sum().item()
print(f"\n测试集准确率: {correct / len(test_ds) * 100:.2f}%")
