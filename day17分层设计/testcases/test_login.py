import unittest
from day15.testcode import login





class TestLogin(unittest.TestCase):
    """
    测试登录函数
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        类级前置
        :return:
        """
        print('我是类级前置，在整个类的测试前执行')
    @classmethod
    def tearDownClass(cls) -> None:
        """
        类级后置
        :return:
        """
        print('我是类级后置，在整个测试类测试完成后执行')

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
    def test_logon_ok(self):
        """
        测试登录成功
        :return:
        """
        #准备测试数据
        test_data = {'username': 'python45','password': 'lemonaban'}
        expect_data = {'code':0,'msg':'登录成功'}
        #2测试步骤：
        res = login(**test_data)
        #3.断言
        self.assertEqual(res,expect_data)

    def test_login_password_error(self):
        """
        测试账号正确，密码错误
        :return:
        """
        print('测试账号正确，密码错误')
    def test_login_username_error(self):
        """
        测试账号错误，密码正确
        :return:
        """
        print('测试账号错误，密码正确')
    def test_login_long_password(self):
        """
        测试账号正确，密码长度过长
        :return:
        """
        print('测试账号正确，密码长度过长')
    def test_login_short_password(self):
        """
        测试账号正确，密码长度过短
        :return:
        """
        print('测试账号正确，密码长度过短')
if __name__ == '__main__':
    unittest.main()