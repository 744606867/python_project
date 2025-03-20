# 文件操作示例

# 打开文件
# file = open("基础数据类型\\file.txt", mode="r",encoding="utf-8")
# for f in file:
#     print(f.strip())

# 追加写入文件
# file = open("基础数据类型\\file.txt", mode="a",encoding="utf-8")
# file.write("hello world"+"\n")
# file.close()

# 使用 with 语句自动关闭文件
# with open("基础数据类型\\file.txt", mode="r",encoding="utf-8") as file:
#     for f in file:
#         print(f.strip())

# 读取非文本文件
# with open("基础数据类型\\pic.jpg", mode="rb") as file:
#     content = file.read()
#     print(content)

# 复制图片文件
# with open("基础数据类型\\pic.jpg", mode="rb") as file:
#     content = file.read()
#     with open("基础数据类型\\pic2.jpg", mode="wb") as file2:
#         file2.write(content)

import os  # 操作系统模块
os.path()   # 路径模块
os.getcwd()  # 获取当前工作目录
os.listdir()  # 列出目录下所有文件和文件夹
os.mkdir()  # 创建目录
os.rmdir()  # 删除目录
os.remove()  # 删除文件
os.rename()  # 重命名文件或目录
os.path.exists()  # 判断文件或目录是否存在
os.path.isfile()  # 判断是否是文件
os.path.isdir()  # 判断是否是目录
os.path.join()  # 路径拼接
os.path.split()  # 路径分割
os.path.splitext()  # 获取文件扩展名
os.path.abspath()  # 获取绝对路径
os.path.dirname()  # 获取目录名
os.path.basename()  # 获取文件名
os.path.getsize()  # 获取文件大小
os.path.getmtime()  # 获取文件修改时间
os.path.getctime()  # 获取文件创建时间
os.path.getatime()  # 获取文件访问时间
os.path.isabs()  # 判断是否是绝对路径
os.path.normpath()  # 规范化路径
os.path.relpath()  # 相对路径
os.path.realpath()  # 真实路径
os.times()  # 获取文件时间戳


# 示例：判断文件或目录是否存在
file_path = "基础数据类型\\file.txt"
if os.path.exists(file_path):
    print(f"{file_path} 存在")
else:
    print(f"{file_path} 不存在")
