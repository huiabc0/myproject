"""

项目入口文件
"""
import  unittest
import unittestreport
if __name__== '__main__':
   #  #实例化一个测试套件对象
   #  ts = unittest.TestSuite()
   # #一个一个添加单元测试
   #  #语法是测试用例类（'单元测试方法'）
   #  # ts.addTest(TestLogin('test_logon_ok'))
   #  # ts.addTest(TestLogin('test_login_password_error'))
   #  #多个添加
   #  ts.addTests(['test_logon_ok','test_login_password_error',])
   #  #运行
   #  runner = unittest.TextTestRunner()
   #  #传入套件
   #  runner.run(ts)
    suite = unittest.defaultTestLoader.discover(start_dir='./testcases') #表示收集当前目录下所有测试用例
    # runner  = unittest.TextTestRunner()
    # runner.run(ts)

    runner = unittestreport.TestRunner(suite, report_dir='./reports',title='测试报告', tester='小丸子', templates=1)
    runner.run()