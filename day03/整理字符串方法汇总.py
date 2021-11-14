"""
7. 使用jupyter notebook 按照课堂讲解的方式，整理如下字符方法

官方文档地址：https://docs.python.org/zh-cn/3/library/stdtypes.html?utm_source=testingpai.com#string-methods

isalpha isdigit islower isupper isspace lower upper strip replace split

"""
# # str.isalpha()
# # 说明  如果字符串中的所有字符都是字母，并且至少有一个字符,返回True，否则返回False，这些字符必须是A-Z，或者a-z，其他字符不行
# # 案例
print('a'.isalpha())    #True
print('A'.isalpha())    #True
print('A1'.isalpha())   #false
print('ABc'.isalpha())  #True

# # str.capitalize()
# # 说明，讲第一个字母大写，其余字符串小写
# # 案例
print('hello'.capitalize())   #输出结果： Hello

# # str.isdigit()
# # 说明：如果字符串中的所有字符都是数字，并且至少有一个字符，返回 True ，否则返回 False
# # 案例
print('111'.isdigit())    # True
print('abd'.isdigit())    # False
print('1b1'.isdigit())    # Flase


# # str.islower()
# # 说明 如果字符串中至少有一个区分大小写的字符且此类字符均为小写则返回 True ，否则返回 False
# # 案例
print('heLlo'.islower())  # False
print('HELLO'.islower())  # False
print('hello'.islower())  # True
print(''.islower())       # False
print('hello'.islower())    #  True 和数字没有关系？


# # str.isupper()
# # 说明 如果字符串中至少有一个区分大小写的字符且此类字符均为大写则返回 True ，否则返回 False
# # 案例
print('HELLO'.isupper())   # True
print('HELoO'.isupper())   # False
print(''.isupper())        # False
print('HELLO111'.isupper())  # False   和数字没有关系？


# str.isspace()
# 说明 如果字符串中只有空白字符且至少有一个字符则返回 True ，否则返回 False 。
# # 案例
print(' '.isspace())  #True
print(''.isspace())   #Flase
print('aaA A'.isspace()) #Flase

# # str.lower()
# # 说明 将字符都转化为小写
# # 案例
print('HELLO'.lower())
print('HEllO'.lower())

# str.upper()
# 说明  将所有小写字母转化为大写
# # 案例
print('hello'.upper())
print('Hello'.upper())

# str.strip([chars])
# 说明  如果不传chars，默认是去除收尾空格，如果传chars，就按照传的规则去除.但是也是去除的收尾
# 案例
print('   spacious   '.strip())   # 去除收尾空格
print('www.example.com'.strip('cmowz.')) # 去除收尾带有comwz的
comment_string = '#....... Section 3.2.1 Issue #32 .......'
print(comment_string.strip('.#! '))   # 去除前后带有.#!
comment_string1 = '%$#.....setion#3.2$.....%'
print(comment_string1.strip('%$#.'))  # 去除前后带有%￥#.


# str.replace(old, new[, count])
# 说明 返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new。 如果给出了可选参数 count，则只替换前 count 次出现
# 案例
comment = 'hello world'
print(comment.replace('hello','da_hai'))
print(comment.replace('o','l',1))

# str.split(sep=None, maxsplit=- 1)
"""说明 切割 sep如果为None，按照默认空格切；如果不为None，按照指定的字符切，maxsplit代表切割次数，如果不指定或者为-1，代表全切，如果指定次数
按照指定次数切
"""
# 案例
comment1= 'hello,beijing,wo lai la'
print(comment1.split())  # 按照默认空格切，返回列表 ['hello,beijing,wo', 'lai', 'la']
print(comment1.split(',')) # 按照逗号切割，返回列表 ['hello', 'beijing', 'wo lai la']
print(comment1.split(',',1))  # 按照逗号切割，返回列表 ['hello', 'beijing,wo lai la']

