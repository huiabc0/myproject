"""
6.使用for打印九九乘法表

提示：

输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）

"""
for i in range (1,10):
    for j in range (1,i+1):
        print('{}*{}={}'.format(j,i,j*i),end='\t')
    print()
