#!/bin/bash

# 创建输出目录
mkdir -p downloaded_images

# 使用Python解析JSON并生成curl命令
python3 << 'EOF'
import json

with open('imglist/imglist.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data.get('data', []):
    photo_name = item.get('photoName', 'unknown')
    large_url = item.get('photoImageUrl', {}).get('large')
    
    if large_url:
        output_path = f"downloaded_images/{photo_name}"
        # 检查文件是否已存在
        import os
        if not os.path.exists(output_path):
            print(f'curl -# -o "{output_path}" "{large_url}"')
EOF
