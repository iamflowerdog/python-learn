import json
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

def download_image(url, filename, output_dir='downloaded_images'):
    """下载单个图片"""
    try:
        # 创建输出目录
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        filepath = os.path.join(output_dir, filename)
        
        # 跳过已存在的文件
        if os.path.exists(filepath):
            print(f'✓ 已存在: {filename}')
            return True
        
        # 下载图片
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f'✓ 已下载: {filename}')
        return True
    except Exception as e:
        print(f'✗ 失败: {filename} - {str(e)}')
        return False

def main():
    # 读取JSON文件
    with open('imglist/imglist.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 提取所有large图片URL和文件名
    tasks = []
    for item in data.get('data', []):
        photo_name = item.get('photoName', 'unknown')
        large_url = item.get('photoImageUrl', {}).get('large')
        
        if large_url:
            # 使用原始照片名作为文件名
            tasks.append((large_url, photo_name))
    
    print(f'准备下载 {len(tasks)} 张图片...\n')
    
    # 使用线程池并发下载（加快速度）
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(download_image, url, filename)
            for url, filename in tasks
        ]
        
        completed = sum(1 for _ in as_completed(futures) if _)
    
    print(f'\n完成: {completed}/{len(tasks)} 张图片')

if __name__ == '__main__':
    main()
