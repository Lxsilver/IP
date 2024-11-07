"""
主程序入口
"""
import os
from core.file_utils import create_date_file

def main():
    """
    主程序函数 - 在当前目录创建日期文件
    """
    # 在当前目录下创建 output 文件夹
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "output")
    
    try:
        file_path = create_date_file(output_dir)
        print(f"文件已创建：{file_path}")
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    main() 