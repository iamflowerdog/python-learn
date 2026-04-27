# PyTorch 入门 Demo

三个由浅入深的小例子，帮你建立 PyTorch 的核心心智模型。

## 安装

```bash
# 在已有的 .venv 中
pip install torch
```

> macOS Apple Silicon 用户：直接 `pip install torch` 即可，会自动支持 MPS（Apple GPU）加速。

## 运行顺序

| 文件 | 学到什么 |
| --- | --- |
| [01_basics.py](01_basics.py) | 张量、运算、GPU/MPS、自动求导 `autograd` |
| [02_linear_regression.py](02_linear_regression.py) | 训练 5 步法：数据 → 模型 → 损失 → 优化器 → 循环 |
| [03_classification.py](03_classification.py) | 自定义 `nn.Module`、`DataLoader`、训练/评估模式 |

```bash
python pytorch_demo/01_basics.py
python pytorch_demo/02_linear_regression.py
python pytorch_demo/03_classification.py
```

## 核心概念速记

1. **Tensor**：多维数组 + GPU 加速 + 自动求导。
2. **autograd**：`requires_grad=True` 的张量参与的运算会被记录成计算图，`loss.backward()` 自动算梯度，存在 `.grad` 里。
3. **训练三件套**（每个 batch 都要做）：
   ```python
   optimizer.zero_grad()   # 清空旧梯度
   loss.backward()         # 反向传播
   optimizer.step()        # 更新参数
   ```
4. **`nn.Module`**：所有模型的基类，重写 `__init__` 定义层、`forward` 定义前向计算。
5. **`model.train()` / `model.eval()`**：切换训练/评估模式（影响 Dropout、BatchNorm 等）。
6. **`with torch.no_grad():`**：推理时关掉 autograd，省显存、跑得快。

## 下一步建议

- 用 `torchvision` 跑一遍 MNIST 手写数字识别（CNN 入门）。
- 学 `Dataset` 自定义数据集。
- 了解 `torch.save` / `torch.load` 保存模型。
