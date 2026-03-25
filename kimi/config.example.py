"""
Kimi API 配置文件模板
复制此文件为 config.py 并填入你的 API Key
"""

# Moonshot API 配置
API_KEY = "your-api-key-here"  # 在此填入你的 API Key
API_URL = "https://api.moonshot.cn/v1/chat/completions"

# 可用的模型列表
MODELS = {
    "kimi-k2.5": "moonshot-v1-8k",  # 标准模型（8K 上下文）
    "kimi-32k": "moonshot-v1-32k",  # 32K 上下文
    "kimi-128k": "moonshot-v1-128k",  # 128K 上下文
}

# 默认模型
DEFAULT_MODEL = "kimi-k2.5"
