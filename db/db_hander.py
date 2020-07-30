from conf import setting
import os
import json


def select_user(user):
    user_path = f'{setting.DB_PATH}/{user}.json'

    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dict = json.load(f)
            return user_dict
    else:
        return False


def save(user_dict):
    # 路径
    user_path = f'{setting.DB_PATH}/{user_dict["user"]}.json'
    # 保存
    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_dict, f, ensure_ascii=False)
        f.flush()





