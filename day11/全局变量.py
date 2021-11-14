class A:
    _arg = 'A'

    def __init__(self,name):
        self.name = name
        print("我是构造方法，在这里初始化_arg")

    def _method(self):
        self.name= '你好'
        print('name = ' +self.name)

    # def _method2(self):
    #     print('arg = ' +self._arg)

a = A('小花')
a._method()
