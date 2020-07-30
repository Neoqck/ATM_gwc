from interface import user_interface
from interface import bank_interface
from interface import shoping_interface
from lib import common
from interface import admin_interface
import datetime

user_info = {
    'user': None
}


def register():
    while True:
        print('---注册---')
        user_name = input('请输入用户名：').strip()
        passwd = input('请输入密码：').strip()
        passwd_d = input('确认密码：').strip()
        # 接口
        flat = user_interface.check_user_interface(user_name)
        if flat:
            print('用户已存在，重新输入！')
            continue
        elif passwd == passwd_d:
            # 接口
            user_interface.register_interface(user_name, passwd)
            print('注册成功!')
            break


def login():
    while True:
        print('---登录---')
        user = input('输入用户名：').strip()
        passwd = input('输入密码：').strip()
        flag, msg = user_interface.login_interface(user, passwd)
        if flag:
            print(msg)
            user_info['user'] = user
            break
        else:
            print(msg)
            break


@common.outter
def transfer():
    while True:
        print('---转账---')
        to_name = input('输入转账目标用户：').strip()
        to_user = user_interface.check_user_interface(to_name)
        if to_user:
            money = input('请输入转账金额：').strip()
            if money.isdigit():
                money = int(money)
                flaw, msg = bank_interface.transfer_interface(to_name, money, user_info['user'])
                if flaw:
                    print(msg)
                    break
                else:
                    print(msg)
                    break
            else:
                print('输入不正确！！')
                continue
        else:
            print('用户不存在，重新输入！')
            continue


@common.outter
def check_balance():
    print('---查询余额---')
    bank_interface.select_money(user_info['user'])


@common.outter
def repayment():
    print('---还款---')
    money = input('请输入还款金额：').strip()
    if money.isdigit():
        money = int(money)
        bank_interface.repayment_interface(user_info['user'], money)
    else:
        print('输入不正确！')


@common.outter
def withdraw_money():
    print('---取款---')
    money = input('请输入取款金额：').strip()
    if money.isdigit():
        money = int(money)
        if money >= 0:
            bank_interface.withdraw_interface(user_info['user'], money)
        else:
            print('必须大于0')
    else:
        print('输入不正确！')


@common.outter
def view_pipelining():
    print('---查看流水---')
    bank_interface.see_worter_interface(user_info['user'])


@common.outter
def shopping():

    # 购买过的商品
    pay_list = []
    num_money = 0
    while True:
        print('---购物---')
        shopping_list = [
            ['QBZ95自动步枪', 999],
            ['M4A1', 999],
            ['手雷', 99],
            ['防弹衣', 299],
            ['尼泊尔军刀', 199],
            ['坦克', 5000000],
            ['神秘武器VIP', 1000000],
        ]

        # 打印商品列表
        for index, i in enumerate(shopping_list):
            print(index, i)
        print('q.退出 w.结账 e.查看已选商品')
        choice = input('请快速配置你的装备：').strip()
        if choice == 'q':
            break

        elif choice == 'w':
            yes = input('是否结账？y/n：')
            if yes == 'y':
                # 调用结账接口
                bank_interface.payment(num_money, user_info['user'])
                # 调用接口保存购买商品
                shoping_interface.save_car(pay_list, user_info['user'])
                break
            elif yes == 'n':
                continue
        elif choice == 'e':
            print('---已选商品---')
            for index, i in enumerate(pay_list):
                print(index, i)
            continue

        # 1.判断是否为数字
        if not choice.isdigit():
            print('输入不合法！！！你还有两次机会')
            continue
        # 2.输入的为字符串，转成int数字型
        choice = int(choice)
        # 3.判断选择是否在范围内
        if 0 <= choice <= len(shopping_list):
            name, money = shopping_list[choice]

            # 4.添加到已选商品
            now_time = datetime.datetime.today()
            now_time = str(now_time)
            # 时间处理操作 2019-11-21 18:45:18.803910  处理为2019-11-21 18:45:18
            now_time = now_time[0:19]
            # 添加时间
            shopping_list[choice].append(now_time)
            pay_list.append(shopping_list[choice])
            # 计价
            num_money += money
            print('添加成功')
            continue
        else:
            print('请选择正确的范围！！！')
            continue


@common.outter
def shopping_cat():
    while True:
        print('---查看购买商品---')
        shoping_interface.select_car(user_info['user'])
        break


def admin():
    while True:
        print('''
        1: 冻结用户
        2：解冻用户
        q: 退出
        ''')
        dict = {
            '1': lock,
            '2': unlock
        }

        choice = input('请输入你的功能：').strip()
        if choice == 'q':
            break
        elif not choice.isdigit():
            print('请输入数字!!')
            continue
        elif choice in dict:
            dict[choice]()
        else:
            print('你的输入有误，重新输入！！！')
            continue


def lock():
    print('---冻结用户---')
    user_name = input('请输入你要冻结的用户名：').strip()
    yes = input('确认冻结该用户？ y/n:')
    if yes == 'y':
        res = admin_interface.lock_interface(user_name)
        print(res)
    elif yes == 'n':
        print('已取消冻结！')
    else:
        print('输入有误，重新输入！')


def unlock():
    print('---解冻用户---')
    username = input('输入你要解冻的用户名：').strip()
    yes = input('确认解冻该用户？ y/n:')
    if yes == 'y':
        res = admin_interface.unlock_interface(username)
        print(res)
    elif yes == 'n':
        print('已取消解冻！')
    else:
        print('输入有误，重新输入！')


def run():
    while True:
        print('''
        1.注册
        2.登录
        3.转账
        4.查询余额
        5.还款
        6.取款
        7.查看流水
        8.购物
        9.查看购买商品
        10.管理员
        q.注销
        ''')
        list_dic = {
            '1': register,
            '2': login,
            '3': transfer,
            '4': check_balance,
            '5': repayment,
            '6': withdraw_money,
            '7': view_pipelining,
            '8': shopping,
            '9': shopping_cat,
            '10': admin
        }
        choice = input('请选择功能编号：').strip()
        if choice == 'q':
            break

        elif choice in list_dic:
            list_dic.get(choice)()

        else:
            print('选择功能有误，请重新输入！')
            continue





















































































