"""
PyTorch 入门 Demo 1：张量（Tensor）基础
========================================
张量是 PyTorch 的核心数据结构，可以理解为「支持 GPU 加速、能自动求导的多维数组」。
"""

import torch

# 1. 创建张量
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.zeros(2, 2)
c = torch.ones(2, 2)
d = torch.randn(2, 2)  # 标准正态分布随机数

print("a =\n", a)
print("d (随机) =\n", d)

# 2. 基本运算（和 NumPy 类似）
print("a + c =\n", a + c)
print("a @ a (矩阵乘法) =\n", a @ a)
print("a.T (转置) =\n", a.T)

# 3. 形状操作
x = torch.arange(12)        # [0, 1, ..., 11]
print("x.shape =", x.shape)
y = x.reshape(3, 4)
print("reshape 成 3x4:\n", y)

# 4. GPU 支持（如果有）
device = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")
print("当前可用设备：", device)
a_on_device = a.to(device)
print("张量被移动到：", a_on_device.device)

# 5. 自动求导（PyTorch 的灵魂）
# requires_grad=True 表示要追踪这个张量上的所有运算，以便求梯度
w = torch.tensor(2.0, requires_grad=True)
loss = (w - 5) ** 2          # 假设这是损失函数 (w-5)^2
loss.backward()              # 反向传播：自动计算 d(loss)/d(w)
print(f"w = {w.item()}, loss = {loss.item()}, dloss/dw = {w.grad.item()}")
# 数学上 d/dw (w-5)^2 = 2(w-5)，w=2 时应为 -6
