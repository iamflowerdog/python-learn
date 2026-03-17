# Kimi AI 对话 Demo

使用 Moonshot API (Kimi) 进行简单对话的示例代码。

## 快速开始

### 1. 配置 API Key

首先复制配置文件模板：

```bash
cp config.example.py config.py
```

然后编辑 `config.py` 文件，填入你的 Moonshot API Key：

```python
API_KEY = "sk-your-actual-api-key"
```

⚠️ **安全提示**: `config.py` 已添加到 `.gitignore`，不会被提交到代码仓库。

### 2. 安装依赖

```bash
pip install requests
```

## 文件说明

- `config.py` - API 配置文件（包含密钥，已忽略提交）
- `config.example.py` - 配置文件模板
- `chat_demo.py` - 完整的对话 demo，包含：
  - 单次对话示例
  - 交互式对话模式（保留对话历史）
- `simple_chat.py` - 最简单的对话示例

## 使用方法

### 1. 运行基本示例

```bash
python chat_demo.py
```

这会运行几个预设的对话示例。

### 2. 运行交互式对话

编辑 `chat_demo.py`，注释掉 `main()`，取消注释 `interactive_chat()`：

```python
if __name__ == "__main__":
    # main()  # 注释掉这行
    interactive_chat()  # 取消注释这行
```

然后运行：

```bash
python chat_demo.py
```

### 3. 运行简单示例

```bash
python simple_chat.py
```

## API 配置

- **API 端点**: `https://api.moonshot.cn/v1/chat/completions`
- **模型选项**:
  - `moonshot-v1-8k` - 8K 上下文
  - `moonshot-v1-32k` - 32K 上下文
  - `moonshot-v1-128k` - 128K 上下文

## 参数说明

- `temperature`: 控制回复的随机性 (0-1)
  - 0.3: 较为确定和一致的回复（推荐）
  - 0.7: 更有创意的回复
  - 1.0: 最大随机性

## 安全提示
✅ API Key 已保存在 `config.py` 中，该文件已添加到 `.gitignore`，不会被提交到代码仓库。

💡 **其他安全方案**：也可以
建议使用环境变量：
```python
import os
API_KEY = os.getenv("MOONSHOT_API_KEY")
```

然后在终端中设置：
```bash
export MOONSHOT_API_KEY="your-api-key"
```
