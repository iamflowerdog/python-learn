# 第一步：准备迷你语料库（一小段文本）
corpus = "我今天很开心 开心的一天 我喜欢开心的感觉"

# 第二步：分词（简化版，按空格拆分，实际NLP分词更复杂）
# 先把所有句子合并，拆成单个词，去重得到所有唯一词
words = corpus.replace(" ", " ").split()  # 拆分所有词
unique_words = list(set(words))  # 去重，得到唯一词列表

# 第三步：构建词表（词→ID映射）
word_to_id = {word: idx for idx, word in enumerate(unique_words)}
id_to_word = {idx: word for word, idx in word_to_id.items()}

print("===== 1. 词表（词→ID） =====")
for word, idx in word_to_id.items():
    print(f"{word} → ID:{idx}")


# 第四步：统计简化版共现（只看相邻词的共现次数）
# 初始化共现矩阵（用字典存储，更直观，避免空矩阵）
co_occurrence = {}
# 先初始化所有词的共现统计为0
for word1 in unique_words:
    co_occurrence[word1] = {word2: 0 for word2 in unique_words}

# 遍历每一个句子（这里按空格拆分的词列表）
token_list = corpus.split()  # 拆分后的词列表：['我','今天','很','开心',...]
for i in range(len(token_list) - 1):
    # 取当前词和下一个相邻词
    current_word = token_list[i]
    next_word = token_list[i + 1]
    # 共现次数+1（双向统计，A和B相邻，B和A也相邻）
    co_occurrence[current_word][next_word] += 1
    co_occurrence[next_word][current_word] += 1


# 第五步：打印共现结果（重点看"开心"的共现）
print("\n===== 2. 简化版共现矩阵（词的相邻出现次数） =====")
# 重点展示"开心"和其他词的共现次数
target_word = "开心"
print(f"\n「{target_word}」和其他词的共现次数：")
for word, count in co_occurrence[target_word].items():
    if count > 0:  # 只打印有共现的词
        print(f"{target_word} ↔ {word}：{count}次")