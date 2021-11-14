# """
# 4.使用print函数和循环结构输出如下由*组成的空心的金字塔图形（选做）
#    *
#   * *
#  *   *
# *******
"""
如果是第一行打印
开始的空格+星号+中间的空格+右边的星号
第一层：开始的空格+星号
中间：开始的空格+星号+中间的空格+右边的星号
中间空格数量=星星数量-2
最后一层：全部都是星号
"""

num = 4
for i in range(num):
    space_num = num-i-1
    start_num = 2*i+1
    if i ==0 or i ==num-1:
        print(' ' * space_num + '*' * start_num)
    else:
        print(' ' * space_num+'*'+' '*(start_num-2)+'*')




