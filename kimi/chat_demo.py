#!/usr/bin/env python3
"""
Kimi AI 对话 Demo
使用 Moonshot API 进行简单的对话
"""

import requests
import json
from config import API_KEY, API_URL

def chat_with_kimi(user_message, model="moonshot-v1-8k"):
    """
    与 Kimi AI 进行对话
    
    Args:
        user_message: 用户消息
        model: 使用的模型，可选：moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k
    
    Returns:
        AI 的回复内容
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ],
        "temperature": 0.3  # 控制回复的随机性，0-1之间
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # 检查是否有 HTTP 错误
        
        result = response.json()
        
        # 提取 AI 的回复
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            return "未收到有效回复"
            
    except requests.exceptions.RequestException as e:
        return f"请求错误: {e}"
    except Exception as e:
        return f"发生错误: {e}"


def main():
    """主函数：演示基本对话"""
    print("=== Kimi AI 对话 Demo ===\n")
    
    # 单次对话示例
    test_messages = [
        "你好，请介绍一下你自己",
        "用Python写一个冒泡排序算法",
        "今天天气怎么样？"
    ]
    
    for msg in test_messages:
        print(f"用户: {msg}")
        response = chat_with_kimi(msg)
        print(f"Kimi: {response}\n")
        print("-" * 60 + "\n")


def interactive_chat():
    """交互式对话模式"""
    print("=== Kimi AI 交互式对话 ===")
    print("输入 'quit' 或 'exit' 退出\n")
    
    conversation_history = []
    
    while True:
        user_input = input("你: ").strip()
        
        if user_input.lower() in ['quit', 'exit', '退出']:
            print("再见！")
            break
            
        if not user_input:
            continue
        
        # 构建包含历史记录的对话
        conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # 调用 API（带历史记录）
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        data = {
            "model": "moonshot-v1-8k",
            "messages": conversation_history,
            "temperature": 0.3
        }
        
        try:
            response = requests.post(API_URL, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            
            if "choices" in result and len(result["choices"]) > 0:
                ai_response = result["choices"][0]["message"]["content"]
                
                # 添加助手回复到历史记录
                conversation_history.append({
                    "role": "assistant",
                    "content": ai_response
                })
                
                print(f"Kimi: {ai_response}\n")
            else:
                print("Kimi: 未收到有效回复\n")
                
        except Exception as e:
            print(f"错误: {e}\n")


if __name__ == "__main__":
    # 运行基本示例
    main()
    
    # 如果想要交互式对话，取消下面的注释
    # interactive_chat()
