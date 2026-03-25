#!/usr/bin/env python3
"""
测试不同的 Kimi 模型
对比各个模型的响应效果
"""

import requests
import time
from config import API_KEY, API_URL, MODELS


def chat_with_model(message, model_name):
    """
    使用指定模型进行对话
    
    Args:
        message: 用户消息
        model_name: 模型名称（完整路径，如 moonshot/kimi-k2.5）
    
    Returns:
        (response_text, elapsed_time) 元组
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": model_name,
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "temperature": 0.3
    }
    
    try:
        start_time = time.time()
        response = requests.post(API_URL, headers=headers, json=data)
        elapsed_time = time.time() - start_time
        
        response.raise_for_status()
        result = response.json()
        
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"], elapsed_time
        else:
            return "未收到有效回复", elapsed_time
            
    except Exception as e:
        return f"错误: {e}", 0


def test_all_models(test_question):
    """
    测试所有可用模型
    
    Args:
        test_question: 测试问题
    """
    print(f"{'='*80}")
    print(f"测试问题: {test_question}")
    print(f"{'='*80}\n")
    
    results = []
    
    for alias, model_name in MODELS.items():
        print(f"🤖 模型: {alias} ({model_name})")
        print(f"{'-'*80}")
        
        response, elapsed_time = chat_with_model(test_question, model_name)
        
        print(f"响应: {response}")
        print(f"⏱️  耗时: {elapsed_time:.2f} 秒")
        print(f"\n")
        
        results.append({
            "alias": alias,
            "model": model_name,
            "response": response,
            "time": elapsed_time
        })
        
        # 稍微延迟，避免请求过快
        time.sleep(0.5)
    
    return results


def compare_models():
    """
    对比测试：用相同问题测试所有模型
    """
    print("\n" + "="*80)
    print("🔍 Kimi 模型对比测试")
    print("="*80 + "\n")
    
    # 测试问题集
    test_questions = [
        "用一句话介绍你自己",
        "Python 和 JavaScript 的主要区别是什么？",
        "写一个计算斐波那契数列的 Python 函数",
    ]
    
    all_results = []
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📋 测试 {i}/{len(test_questions)}")
        results = test_all_models(question)
        all_results.append({
            "question": question,
            "results": results
        })
        
        # 在不同问题之间多等一会
        if i < len(test_questions):
            time.sleep(1)
    
    # 打印总结
    print("\n" + "="*80)
    print("📊 测试总结")
    print("="*80 + "\n")
    
    # 计算平均响应时间
    avg_times = {}
    for model_alias in MODELS.keys():
        times = []
        for test in all_results:
            for result in test["results"]:
                if result["alias"] == model_alias:
                    times.append(result["time"])
        avg_times[model_alias] = sum(times) / len(times) if times else 0
    
    print("平均响应时间:")
    for alias, avg_time in sorted(avg_times.items(), key=lambda x: x[1]):
        print(f"  • {alias:25s}: {avg_time:.2f} 秒")


def test_single_model(model_alias=None):
    """
    测试单个模型（交互式）
    
    Args:
        model_alias: 模型别名，如 kimi-k2.5
    """
    if model_alias is None:
        print("\n可用模型:")
        for i, (alias, model_name) in enumerate(MODELS.items(), 1):
            print(f"  {i}. {alias} ({model_name})")
        
        choice = input("\n请选择模型编号 (1-5): ").strip()
        try:
            model_alias = list(MODELS.keys())[int(choice) - 1]
        except (ValueError, IndexError):
            print("无效选择，使用默认模型 kimi-k2.5")
            model_alias = "kimi-k2.5"
    
    if model_alias not in MODELS:
        print(f"错误: 模型 {model_alias} 不存在")
        return
    
    model_name = MODELS[model_alias]
    print(f"\n使用模型: {model_alias} ({model_name})")
    print("输入 'quit' 或 'exit' 退出\n")
    
    while True:
        question = input("你: ").strip()
        
        if question.lower() in ['quit', 'exit', '退出']:
            print("再见！")
            break
        
        if not question:
            continue
        
        print(f"\n{model_alias}: ", end="", flush=True)
        response, elapsed_time = chat_with_model(question, model_name)
        print(response)
        print(f"⏱️  ({elapsed_time:.2f}s)\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # 命令行模式
        if sys.argv[1] == "compare":
            # 对比所有模型
            compare_models()
        elif sys.argv[1] == "test":
            # 测试单个模型
            model = sys.argv[2] if len(sys.argv) > 2 else None
            test_single_model(model)
        else:
            print("用法:")
            print("  python test_models.py compare     # 对比所有模型")
            print("  python test_models.py test [模型别名]  # 测试单个模型")
    else:
        # 默认运行对比测试
        compare_models()
