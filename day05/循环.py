# break
# break是跳出整个循环体
# ls = [60, 59, 78, 80, 56, 55]
# for i in ls:
#     if i < 60:
#         print('有同学不及格')
#         break

#断点不能只打在第一行
#  contine，不会影响else语句，可以通过else检查循环是否正常执行
a =1
# for i in range(10):
#     if i % 2 !=0:
#         continue
#     print(i)

# for i in range(10):
#     if i % 2 !=0:
#         break
#     print(i)

# for i in range(10):
#     if i%2!=0:
#         continue
#     print(i)
# else:
#     print('循环正常结束')

list = [1,2,3,4,5]
for i in list:
    if i ==3:
       list.remove(i)
print(list)