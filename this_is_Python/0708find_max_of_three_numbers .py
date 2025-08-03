
"""
请用户输入三个不同的整数, 输入时用空格隔开, 利用条件语句判断出这三个整数中的最大值
"""
while True:
    user_input = input('请用户输入三个不同的整数, 输入时用空格隔开: ').strip()
    num = user_input.split()                                       #利用空格分隔出来整数

    if len(num) != 3:                                                  #判断字符串长度是否为3
        print('请输入三个整数，输入时用空格隔开:')
        continue

    else:                                                                  #赋值并判断是否是整数
        a, b, c = map(int, num)

    if a > b and a > c:                                               #比大小
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
    break