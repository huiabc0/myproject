"""

计算BMI值
输入体重身高
6.按要求编写程序,简单版本挑其中一种标准写，比如国内标准。


"""
#接受输入用户信息
weight = float(input('请输入你的体重(kg):'))
height = float(input('请输入你的身高(米):'))
#计算BMI值
bmi = weight/(height**2)
#评价信息
wto = ''
cto =''
if bmi < 18.5:
    wto = '偏瘦'
    cto = '偏瘦'
elif 18.5<=bmi< 24:
    wto = '正常'
    cto = '正常'
elif 24<=bmi<25:
    wto = '正常'
    cto = '偏胖'
elif 25<=bmi<28:
    wto = '偏胖'
    cto = '偏胖'
elif 28<=bmi<30:
    wto = '偏胖'
    cto = '肥胖'
else:
    cto = '肥胖'
    wto = '肥胖'
print('您的BMI={:.2f}，国际标准{},国内标准{}'.format(bmi,wto,cto))