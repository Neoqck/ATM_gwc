import hashlib
from core import src


def get_md5(pwd):
    val = '王氏家族终极密码'
    md5 = hashlib.md5()
    md5.update(val.encode('utf-8'))
    md5.update(pwd.encode('utf-8'))
    res = md5.hexdigest()
    return res


def outter(func):

    def inner(*args, **kwargs):
        while True:
            if src.user_info['user']:
                res = func(*args, **kwargs)
                return res
            else:
                print('请先登录！')
                break
    return inner




