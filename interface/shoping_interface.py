from db import db_hander

# 保存购物车
def save_car(shopping_list, user):
    user_dict = db_hander.select_user(user)
    # 添加到字典
    user_dict['shop_car'].append(shopping_list)
    # 保存
    db_hander.save(user_dict)


# 查看购物车
def select_car(user):
    user_dict = db_hander.select_user(user)
    car_list = user_dict['shop_car']
    # for index, i in enumerate(car_list):
    #     print(index, i)
    for line in car_list:
        for index, i in enumerate(line):
            print(index, i)

