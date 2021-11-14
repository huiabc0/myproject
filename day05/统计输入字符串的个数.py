"""
2.编写程序实现，用户从键盘输入一行字符，编写一个程序，统计并输出其中英文字符(不考虑中文)，数字，空格和其他字符的个数。
提示：遍历字符串，通过字符串方法判断字符类型，然后统计

"""
s = input('请输入一行字符串:')
alpha,num,space,other=0,0,0,0
for i in s:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        num += 1
    elif i.isspace():
        space += 1
    else:
        other += 1
print('英文字符个数为{},数字字符个数为{},空格字符个数为{},其他字符个数为{}'.format(alpha,num,space,other))
