import logging
#1.创建日志器
logger = logging.getLogger('py45')
logger.setLevel(logging.DEBUG)  #给日志器设置等级

#2创建日志处理器
#创建一个控制台处理器，用于将日志输出控制台
console = logging.StreamHandler()
console.setLevel("INFO")

#创建日志文件处理器，将日志输出到文件中
file_console = logging.FileHandler(filename='1.log',encoding='utf-8',mode='a')
file_console.setLevel('WARNING')

3.#创建格式化处理器
formatter = logging.Formatter(fmt='%(asctime)s-[%(filename)s--->line:%(lineno)d]-%(levelname)s:%(message)s',)

#4将格式化器设置到处理器上
console.setFormatter(formatter)
file_console.setFormatter(formatter)

#5给日志器添加处理器
logger.addHandler(console)
logger.addHandler(file_console)

#6记录日志
logger.debug('ww')
logger.warning('你再不处理试试')