print("今天我要去购物，Let's go!")
ans = input("售货员说：欢迎光临\n请问你有我们的会员吗(Y/N)")
if ans == 'Y':
    print('shopping')
    cost = float(input('今天本超市有活动，请问消费金额是多少 '))
    if cost <= 1000:
        print(f'恭喜，获得键盘！')
    elif cost <= 500:
        print(f'恭喜，获得鼠标！')
    elif cost <= 100:
        print(f'恭喜，获得消费券！')

else:
    ans = input(f'我们是会员制超市，请问是否需要办理会员？（Y/N)')
    if ans == 'Y':
        print(f'正在办理中')
    else:
        print('对不起，没有会员不可以购物')
