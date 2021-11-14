import unittest
# from ddt import ddt,data
from day17分层设计.testcode import login
from unittestreport  import ddt,list_data
from day17分层设计.common.data_hander import get_data_excel



# 测试数据集
# cases = [
# {'title':'登录成功','request':{'username':'python45','password':'lemonaban'},'expect':{'code':0,'msg':'登录成功'}},
# {'title':'密码错误','request':{'username':'python45','password':'lemonban1'},'expect':{'code':1,'msg':'账号或者密码不正确'}},
# {'title':'账号错误','request':{'username':'python415','password':'lemonban'},'expect':{'code':1,'msg':'账号或者密码不正确'}},
# {'title':'密码过短','request':{'username':'python45','password':'lemon'},'expect':{'code':1,'msg':'密码长度在6-18位之间'}},
# {'title':'密码过长','request':{'username':'python45','password':'lemonban123456789012345678'},'expect':{'code':1,'msg':'密码长度在6-18位之间'}},
# ]

cases = get_data_excel('.\\testdata\\testdata.xlsx', 'login')

@ddt
class TestLogin(unittest.TestCase):
    """
    测试登录函数
    """

    @classmethod
    def setUpClass(cls) -> None:

        print('login函数开始测试')
    @classmethod
    def tearDownClass(cls) -> None:
        print('login函数结束测试')

    def setUp(self) -> None:
        """
        方法级前置
        :return:
        """
        print('===我会在每个测试执行前执行===')
    def tearDown(self) -> None:
        """
        方法级后置
        :return:
        """
        print('====我会在每个测试执行后执行===')

    @list_data(cases)           #不同：注意：list_data装饰器，接收可迭代对象不需要解包，不需要加*
    def test_logon(self,case):
        print('{}开始测试'.format(case['title']))
        #2测试步骤：
        res = login(**eval(case['request']))
        #3.断言
        self.assertEqual(res,eval(case['expect']))

