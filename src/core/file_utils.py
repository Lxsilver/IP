"""
文件操作相关的工具函数
"""
from datetime import datetime
import os

def create_date_file(directory: str) -> str:
    """
    在指定目录创建包含当前日期的文本文件
    
    Args:
        directory: 目标目录路径
    
    Returns:
        str: 创建的文件路径
    """
    # 确保目录存在
    os.makedirs(directory, exist_ok=True)
    
    # 生成文件名：date_年月日.txt
    current_date = datetime.now().strftime("%Y%m%d")
    filename = f"date_{current_date}.txt"
    file_path = os.path.join(directory, filename)
    
    # 写入文件
    with open(file_path, 'w') as f:
        f.write(f"当前日期：{current_date}")
    
    return file_path 