# ls = ['心蓝',18,['健身','妹子'],[['刘德华',56],['张学友',57]]
# print(ls[2][1])


# s='0123456789'
# print(s[::2])
# print(s[::-2])
# print(s[-2:-8:-1])
# print(s[-2:-7:1])
# print(s[5::2])
# print(s[5:9:-2])
# print(s[5:1:-2])

#接受输入用户信息
try:
    weight = float(input('请输入你的体重(公斤):'))
except ValueError:
    print('体重输入有误')
    exit(-1)

try:
    height = float(input('请输入你的身高(厘米):')) / 100
except ValueError:
    print("身高输入错误")
    exit(-1)

if height<=0 or weight<=0:
    print('身高或者体重不能为零')
    exit(-1)

#计算BMI值
BMI=weight/height**2

internal=''
external=''
if BMI<18.5:
    internal = '偏瘦'
elif 18.5<=BMI<24:
    internal = '正常'
elif 24<=BMI<28:
    internal = '偏胖'
else:
    internal = '肥胖'

if BMI < 18.5:
    external = '偏瘦'
elif 18.5<=BMI<25:
    external = '正常'
elif 25<=BMI<30:
    external = '偏胖'
else:
    external = '肥胖'


print('BIM值为 {:.2f} 国内{}, 国际{}'.format(BMI, internal,external))
