# 代码生成时间: 2025-09-21 08:15:49
import os
import requests
from typing import List, Tuple

# 定义一个异常类，用于处理重命名过程中的错误
class RenameError(Exception):
    pass

"""
批量文件重命名工具

该工具使用requests框架向服务器发送重命名请求，并处理服务器响应。"""

class BatchFileRenamer:
    def __init__(self, base_url: str):
        """
        初始化BatchFileRenamer对象

        :param base_url: 服务器的基本URL
        """
        self.base_url = base_url

    def rename_file(self, file_path: str, new_name: str) -> bool:
        """
        发送重命名请求到服务器

        :param file_path: 文件路径
        :param new_name: 新文件名
        :return: 如果重命名成功返回True，否则返回False
        """
        try:
            url = f"{self.base_url}/rename"
            payload = {"file_path": file_path, "new_name": new_name}
            response = requests.post(url, json=payload)
            response.raise_for_status()  # 检查响应状态码
            return True
        except requests.RequestException as e:
            print(f"请求失败：{e}")
            return False
        except Exception as e:
            raise RenameError(f"重命名过程中发生错误：{e}")

    def batch_rename(self, file_paths: List[str], new_names: List[str]) -> Tuple[List[bool], List[str]]:
        """
        批量重命名文件

        :param file_paths: 文件路径列表
        :param new_names: 新文件名列表
        :return: 成功重命名的文件列表和失败的文件列表及其错误消息
        """
        success_files = []
        failed_files = []
        for file_path, new_name in zip(file_paths, new_names):
            success = self.rename_file(file_path, new_name)
            if success:
                success_files.append(file_path)
            else:
                failed_files.append((file_path, f"重命名失败：{new_name}"))
        return success_files, failed_files

# 示例用法
if __name__ == "__main__":
    base_url = "https://example.com/api"
    renamer = BatchFileRenamer(base_url)

    file_paths = ["/path/to/file1.txt", "/path/to/file2.txt"]
    new_names = ["new_file1.txt", "new_file2.txt"]

    success_files, failed_files = renamer.batch_rename(file_paths, new_names)
    print("成功重命名的文件：", success_files)
    print("失败的文件及其错误消息：", failed_files)