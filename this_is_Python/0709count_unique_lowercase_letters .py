"""
实现程序:
用户输入一串小写的英文字母, 求出英文字母有几种？并格式化输出

例如：
输入 agbcppdcdho    输出：其中有 a b c d g h o p 8种英文字母
"""

while True:
    user_input = input('请输入一串小写英文字母: ').strip()

    if user_input.islower() and user_input.isalpha():    #判断字符串是否是小写英文字母
        s = sorted(set(user_input))                             #转成集合去重并排序
        letter = ' '.join(s)                                            #转成空格显示

        print(f'其中有{letter} {len(s)}种英文字母')
        break
    else:
        print('请输入“小写英文字母！')