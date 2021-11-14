"""
1.编写如下程序
使用while循环实现输出2 - 3 + 4 - 5 + 6 ... + 100 的和

2.编写如下程序
用户输入考试成绩，当分数高于90（包含90）时打印A；否则如果分数高于80（包含80）时打印B；否则如果当分数高于70（包含）时打印C；否则如果当分数高于60（包含60）时打印D；其他情况就打印E

3.编写如下程序
假设一年的定期利率为3.52%，需要几年才能让定期存款连本带息的翻一番（例如：需要几年10000才能变成20000）

4.编写如下程序
从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出
提示：
a. 1!等于 1
b. 2!等于 1*2
c. 3!等于 1*2*3
d. n!等于 1*2*3*...*n

"""

num = 2
total = 0
while  num<=100:
    if num%2==0:
        total+=num
    elif num %2 == 1:
        total-=num
    num+=1
print('最终的和{}'.format(total))

while True:
    score = (input("请输入考试成绩"))
    try:
        score = float(score)
        break
    except:
        print("你输入的{}格式不正确".format(score))
res = ''
if score>=90:
        res = '成绩为A'
elif 80<= score<90:
        res = '成绩为B'
elif 70<=score<80:
        res = '成绩为C'
elif 60 <= score < 70:
        res = '成绩为D'
else:
        res = '成绩为E'
print('考试成绩为{}'.format(res))

num= int(input('请输入数字'))
num