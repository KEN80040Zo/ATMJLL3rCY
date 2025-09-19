# 代码生成时间: 2025-09-19 18:49:54
import hashlib
import sys

"""
哈希值计算工具
这个程序允许用户输入字符串，并计算其MD5、SHA1和SHA256哈希值。
"""


# 函数：计算哈希值
def calculate_hash(string, hash_type):
    # 根据哈希类型创建不同的哈希对象
    if hash_type == 'md5':
        hash_obj = hashlib.md5()
    elif hash_type == 'sha1':
        hash_obj = hashlib.sha1()
    elif hash_type == 'sha256':
        hash_obj = hashlib.sha256()
    else:
        raise ValueError("Unsupported hash type. Supported types are 'md5', 'sha1', 'sha256'.")

    # 更新哈希对象以包含输入的字符串
    hash_obj.update(string.encode('utf-8'))

    # 返回十六进制格式的哈希值
    return hash_obj.hexdigest()


# 主函数
def main():
    if len(sys.argv) < 3:
        print("Usage: python hash_calculator.py <string> <hash_type>")
        sys.exit(1)

    input_string = sys.argv[1]
    hash_type = sys.argv[2]

    # 计算哈希值
    try:
        hash_value = calculate_hash(input_string, hash_type)
        print(f"{hash_type.upper()} hash of '{input_string}' is: {hash_value}")
    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()