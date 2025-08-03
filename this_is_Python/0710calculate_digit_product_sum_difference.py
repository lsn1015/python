
"""
实现程序：请用户输入一个正整数 n, 程序计算并输出该整数「各位数字之积」与「各位数字之和」的差

示例:
输入: n = 234
输出: 15

解释:
各位数之积 = 2 * 3 * 4 = 24
各位数之和 = 2 + 3 + 4 = 9
结果 = 24 - 9 = 15
"""
user = input('Please enter an positive integer: n = ').strip()
total_sum = 0
total_product = 1

if user.isdigit():
    for i in user:
        total_sum += int(i)
        total_product *= int(i)
    print(total_product - total_sum)
else:
    print('please enter a valid integer!')


