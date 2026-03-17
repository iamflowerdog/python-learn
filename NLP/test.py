# 第一步：定义情绪关键词库（相当于给计算机的"情绪词典"）
positive_words = ["开心", "快乐", "棒", "好", "满意", "喜欢", "棒极了", "舒服"]
negative_words = ["难过", "生气", "差", "坏", "不满意", "讨厌", "糟透了", "难受"]

# 第二步：获取用户输入的文本
user_text = input("请输入一句话，我来分析你的情绪：")

# 第三步：统计正面/负面关键词出现的次数
positive_count = 0
negative_count = 0

# 遍历正面关键词，看看有没有出现在用户输入里
for word in positive_words:
    if word in user_text:
        positive_count += 1

# 遍历负面关键词，看看有没有出现在用户输入里
for word in negative_words:
    if word in user_text:
        negative_count += 1

# 第四步：根据统计结果判断情绪
if positive_count > negative_count:
    print(f"😃 你的情绪是正面的！我找到{positive_count}个开心的词，{negative_count}个不开心的词。")
elif negative_count > positive_count:
    print(f"😞 你的情绪是负面的！我找到{negative_count}个不开心的词，{positive_count}个开心的词。")
else:
    print(f"😐 你的情绪比较中性，我没找到明显的开心或不开心的词。")