"""
3.使用print函数和循环结构输出如下由*组成的金字塔（可以尝试根据层数动态输出）
    *
   ***
  *****
 *******

"""
# for i in range(0, 4):
#     for j in range(0, 7):
#         if abs(3 - j) > i:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print('')




"""
1.先写死,根据题目总共4层
2.计算space_num和start_num的数量
"""
num = 4
for i in range(4):
    space_num = 4-i-1
    start_num = 2*i+1
    print(' '*space_num+'*'*start_num)
# print(' '*3+'*'*1)
# print(' '*2+'*'*3)
# print(' '*1+'*'*5)
# print(' '*0+'*'*7)

