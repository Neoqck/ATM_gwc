from db import db_hander
from lib import common


# 查看用户是否存在接口，存在返回True 和字典，不存在返回False
def check_user_interface(user):
    user_dict = db_hander.select_user(user)
    if user_dict:
        return user_dict
    else:
        return False


# 注册接口
def register_interface(user, passwd):
    # 调用接口，加密
    pwd = common.get_md5(passwd)

    # 把用户所有信息做成一个字典，然后调用接口保存
    user_dict = {
        'user': user,
        'pwd': pwd,
        'balance': 10000,
        'worter': [],
        'shop_car': [],
        'lock': True
    }

    db_hander.save(user_dict)

    return f'{user_dict["user"]}用户注册成功！'

# 登录接口
def login_interface(user, passwd):
    user_dict = db_hander.select_user(user)
    passwd = common.get_md5(passwd)
    # 如果用户存在
    if user_dict:
        # 如果用户没有被锁
        if user_dict['lock'] == True:
            # 如果密码正确
            if passwd == user_dict['pwd']:
                return True, '登录成功！'
            else:
                return False, '用户名或密码不正确，重新输入！'

        else:
            return False, '用户已被冻结，请联系管理员！'

    else:
        return False, '用户名或密码不正确，重新输入！'























