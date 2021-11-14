def login(username,password):
    """
    登录校验的函数
    :param username:
    :param password:
    :return:
    """
    if 6 <= len(password)<=18:
        if username=='python45' and password=='lemonaban':
            return {'code':0,'msg':'登录成功'}
        else:
            return {'code': 1, 'msg': '账号或者密码不正确'}
    else:
        return {'code': 1, 'msg': '密码'}