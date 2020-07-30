from db import db_hander
import datetime


# 转账接口
def transfer_interface(to_name, money, user):
    to_user_dict = db_hander.select_user(to_name)
    user_dict = db_hander.select_user(user)

    if to_name != user:
        # 判断转账的钱是否大于余额
        if 0 <= money <= user_dict['balance']:
            # 加减钱的操作：
            user_dict['balance'] -= money
            to_user_dict['balance'] += money

            # 拼接
            my = user_dict['balance']
            to = to_user_dict['balance']
            time = datetime.datetime.today()
            msg = f'【{user}】用户给【{to_name}】用户转账【{money}】元，当前余额【{my}】元    {time}'
            flg = f'【{to_name}】用户收到【{user}】用户转账【{money}】元，当前余额【{to}】元    {time}'
            # 添加到流水信息
            user_dict['worter'].append(msg)
            to_user_dict['worter'].append(flg)

            # 保存数据
            db_hander.save(user_dict)
            db_hander.save(to_user_dict)

            return True, msg
        else:
            msg = '余额不足'
            return False, msg
    else:
        return False, '不允许给自己转账！'


# 查看余额
def select_money(user):
    user_dict = db_hander.select_user(user)
    money = user_dict['balance']
    return print('当前余额为【%s】' % money)


# 还款接口
def repayment_interface(user, money):
    user_dict = db_hander.select_user(user)
    # 加钱操作
    user_dict['balance'] += money

    a = user_dict['balance']
    time = datetime.datetime.today()
    msg = f'【{user}】用户还款【{money}】元成功，当前余额【{a}】元    {time}'
    # 添加到流水信息
    user_dict['worter'].append(msg)
    # 保存更新
    db_hander.save(user_dict)

    return print(msg)


# 取款接口
def withdraw_interface(user, money):
    while True:
        user_dict = db_hander.select_user(user)
        # 判断余额是否足够
        if money <= user_dict['balance']*1.05:
            # 减钱操作，手续费
            money_s = money*0.05
            user_dict['balance'] -= money*1.05

            a = user_dict['balance']
            time = datetime.datetime.today()
            msg = f'【{user}】用户取款【{money}】元成功，手续费5%【{money_s}】元，当前余额【{a}】元    {time}'

            # 添加到流水信息
            user_dict['worter'].append(msg)

            # 保存更新
            db_hander.save(user_dict)
            return print(msg)

        else:
            print('余额不足！!')
            break


# 查看流水
def see_worter_interface(user):
    user_dict = db_hander.select_user(user)
    worter = user_dict['worter']
    for i in worter:
        print(i)


# 结账接口
def payment(num_money, user):
    while True:
        user_dict = db_hander.select_user(user)
        if num_money <= user_dict['balance']:
            # 减钱的操作
            user_dict['balance'] -= num_money

            a = user_dict['balance']
            time = datetime.datetime.today()
            msg = f'【{user}】用户购买商品成功，消费【{num_money}】元，当前余额【{a}】元    {time}'
            # 记录流水
            user_dict['worter'].append(msg)
            # 保存信息
            db_hander.save(user_dict)
            print(msg)
            break
        else:
            print('余额不足，请充值！！！')
            break




























