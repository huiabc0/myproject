"""
1. 编写程序实现，在程序中预设一个0~9之间的整数，让用户通过键盘输入所猜的数，如果大于预设的数，显示“遗憾，太大了”，
小于预设的数，显示“遗憾，太小了”，如此循环，直至猜中该数，显示“预测N次，你猜中了！”，其中N是用户输入数字的次数。

提示：使用while无限循环，当猜中时break

"""

import random

targeNum = random.randint(0, 9)  # 目标数

guessCount = 0  # 用户猜测次数

while True:

    guessNum = int(input('请输入数字:'))  # 获取用户输入数
    guessCount += 1  # 用户猜测计数
    if guessNum > targeNum:
        print('遗憾，太大了')
        continue
    elif guessNum < targeNum:
        print('遗憾，太小了')
        continue
    elif guessNum == targeNum:
        print('你猜中了，用户输入次数为{}'.format(guessCount))
        break
    else:
        print('输入错误')
        continue
