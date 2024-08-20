# 变量
# 变量定义
x = 10
y = 3.14
name = "Alice"

# 数据类型展示
data_types = {
    "整数 (int)": x,
    "浮点数 (float)": y,
    "字符串 (str)": name,
    "布尔值 (bool)": True
}

for description, value in data_types.items():
    print(f"{description}: {type(value)}")

