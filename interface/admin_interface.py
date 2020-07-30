from db import db_hander


# 冻结用户
def lock_interface(user_name):
    user_dict = db_hander.select_user(user_name)
    if user_dict:
        user_dict['lock'] = False
        # 保存更新
        db_hander.save(user_dict)
        return '已冻结'
    else:
        return '不存在该用户，重新输入！'


# 解冻用户
def unlock_interface(user_name):
    user_dict = db_hander.select_user(user_name)
    if user_dict:
        user_dict['lock'] = True
        # 保存更新
        db_hander.save(user_dict)
        return '已解冻'
    else:
        return '不存在该用户，重新输入'














