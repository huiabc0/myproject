"""
第1题 使用异常处理改写成绩评价代码，使程序可以输入非法字符
"""
#接受输入用户信息
# while True:
#     score = input('请输入你的成绩')
#     try:
#         score = float(score)
#         break
#     except:
#         print('输入成绩{}格式不正确'.format(score))
#
# res = ''
# if score < 40:
#     res = '成绩评价为:E'
# elif score < 60 and score >= 40:
#     res = '成绩评价为:D'
# elif 60 <= score <= 75:
#     res = '成绩评价为:C'
# elif 75 <= score <= 85:
#     res = '成绩评价为:B'
# elif 85 <= score <= 100:
#     res = '成绩评价为:A'
#
# print('你的成绩为{}'.format(res))


"""
第2题 实现`is_odd()`函数，接受一个整数参数，如果为奇数，返回`True`，否则返回False。 
"""

# def is_odd(num):
#     if num % 2 !=0:
#         return True
#     else:
#         return False
#
# is_odd(1)

"""
第3题 实现`is_num()`函数，参数为一个字符串，如果这个字符串属于整数或浮点数，则返回`True`，否则返回`False`
"""


# def is_num(str_num):
#     try:
#         float(str_num)
#     except:
#         return False
#     else:
#         return True


"""
第4题 实现`multi()`函数，最少接收两个整数参数，返回所有整数参数的乘积。 
"""

# def multi(a,b,*args):
#     a *=b
#     for i in args:
#         a *=i
#     print(a)
#
# multi(2,3,4,5,6,7)


# """
# 第5题 实现`is_prime()`函数，参数为整数，要有异常处理。如果整数时质数，返回True，否则返回False
# """

def is_prime(num):
    try:
        if num <= 1:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False
    except:
        raise ValueError('请输入一个整数')
    return True
is_prime(5)