"""
PyTorch 入门 Demo 2：用神经网络拟合一条直线 y = 2x + 1
======================================================
这是「最小可运行」的训练流程，包含 PyTorch 训练的 5 个核心步骤：
    1. 准备数据
    2. 定义模型
    3. 定义损失函数 + 优化器
    4. 训练循环（前向 -> 计算损失 -> 反向 -> 更新参数）
    5. 查看结果
"""

import torch
from torch import nn

# ---------- 1. 准备数据：生成带噪声的 y = 2x + 1 ----------
torch.manual_seed(42)
x = torch.linspace(-1, 1, 100).unsqueeze(1)   # shape: [100, 1]
y = 2 * x + 1 + 0.2 * torch.randn(x.size())   # 加点噪声更真实

# ---------- 2. 定义模型：一个线性层 y = wx + b ----------
model = nn.Linear(in_features=1, out_features=1)

# ---------- 3. 损失函数 & 优化器 ----------
loss_fn = nn.MSELoss()                                  # 均方误差
optimizer = torch.optim.SGD(model.parameters(), lr=0.1) # 随机梯度下降

# ---------- 4. 训练循环 ----------
for epoch in range(200):
    # 前向传播
    y_pred = model(x)
    loss = loss_fn(y_pred, y)

    # 反向传播 + 更新参数（这三步是固定套路！）
    optimizer.zero_grad()   # 清空上一轮的梯度
    loss.backward()         # 计算梯度
    optimizer.step()        # 用梯度更新参数

    if (epoch + 1) % 20 == 0:
        w = model.weight.item()
        b = model.bias.item()
        print(f"Epoch {epoch+1:3d} | loss={loss.item():.4f} | w={w:.3f}, b={b:.3f}")

# ---------- 5. 最终结果 ----------
print("\n训练完成！模型学到的参数：")
print(f"  w ≈ {model.weight.item():.3f} (真实值 2)")
print(f"  b ≈ {model.bias.item():.3f} (真实值 1)")
