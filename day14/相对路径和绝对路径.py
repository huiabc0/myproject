#绝对路径
#C:/windoes/.../xxx
# D:\pythonProject3\day14\test.txt
# 前面加r 表示字符串原样输出

"""
相对路径：

"""

with open (r'D:\pythonProject3\day14\test.txt','r',encoding='utf')as f:
    print(f.read())

"""
读取大文件，不是一次性读取，逐行读取用readline，一次读取一行，如果中间有空格，也会打印空格
用readlines读取一次性读完所有的行 以列表形式返回
凡是以for循环的都是可迭代对象

"""


"""


"""