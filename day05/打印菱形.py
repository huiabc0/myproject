"""
5.使用print函数和循环结构输出如下由*组成的菱形（选做）
  *
 ***
 *****
*******
 *****
 ***
  *
思路：
拆分任务上下两部分
上面是一个实心金字塔
下面是一个倒的实心金字塔
计算每层的星星和空格的数量
4层的正三角形+3层的到三角形
下面的三角形整体往右偏移一个空格
"""
num = 4
for i in range(num):
    space_num = num-i-1
    start_num = 2*i+1
    print(' ' * space_num + '*' * start_num)

#1.到三角形
# print(' '*0+'*'*5)
# print(' '*1+'*'*3)
# print(' '*2+'*'*1)

for i in range(num-1):
    space_num = i+1
    start_num = (num-1-i)*2-1
    print(' '*space_num+'*'*start_num)
#print(i,(num-1-i)*2-1)