import logging

#设置日志
logging.basicConfig(
    #设置日志等级
    # level=logging.DEBUG,
    # 1.日志会根据设置等级级别的优先级输出，级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
    level=logging.WARNING,
    format='%(asctime)s-[%(filename)s--->line:%(lineno)d]-%(levelname)s:%(message)s', #设置输出格式
    datefmt='%Y/%m/%d %H:%M:%S',
    #输出到文件中
    filename='1.txt',
    filemode='a'
)

logging.debug("我是debug信息")
logging.info("我是info信息")
logging.warning("我是warning信息")
logging.error("我是error信息")
logging.critical("我是critical信息")
logging.log(logging.WARNING, "我是log信息")
