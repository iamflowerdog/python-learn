#!/usr/bin/env python3
"""
最简单的 Kimi AI 对话示例
"""

import requests
from config import API_KEY, API_URL

# 你想问的问题
question = "你好，请用一句话介绍你自己"

# 发送请求
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "model": "moonshot-v1-8k",
    "messages": [
        {"role": "user", "content": question}
    ]
}

response = requests.post(API_URL, headers=headers, json=data)
result = response.json()

# 打印结果
print(f"问: {question}")

# 检查是否有错误
if "error" in result:
    print(f"错误: {result['error']}")
elif "choices" in result:
    print(f"答: {result['choices'][0]['message']['content']}")
else:
    print(f"未知响应: {result}")
