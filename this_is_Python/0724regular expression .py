import re
"""
匹配string中所有单词的开头字母

string = 'Then your voice calls me back like a wake up call'
"""
string = 'Then your voice calls me back like a wake up call'
w = [word[0] for word in string.split()]
print(w)

matches = re.findall(r'\b\w',string)
print(matches)

"""
提取string中以m或t开头的单词, 忽略大小写

string = 'This module provides regular expression matching operations similar to those found in Perl'
"""
string = 'This module provides regular expression matching operations similar to those found in Perl'

###1
n = [word for word in string.split() if word.lower()[0] in ('m','t')]
print(f'list expression: ', n)
###2
matches = re.findall(r'\b[mMtT]\w*',string, flags=re.IGNORECASE)
print(f'regular comprehension: ', matches)
###3
words = string.split()
matches = list(filter(lambda word: word.lower().startswith(('m','t')), words))
print(f'lambda function: ', matches)

"""
提取string中连续5个以上的数字

string = '小明202208月见义勇为, 替小红当了3456789点暴击伤害, 快打110报警, 抓住那个劫匪'
"""
string = '小明202208月见义勇为, 替小红当了3456789点暴击伤害, 快打110报警, 抓住那个劫匪'
matches = re.findall(r'\d{5,}',string)  #\d：匹配任意数字（等价于 [0-9]）。{5,}：表示前面的模式（\d）至少重复5次（即连续5个或更多数字）
print(f'regular comprehension: ', matches)

"""
提取出string中的所有域名(比如: http://www.iteoem.com/ 就是域名)

string = '''
http://www.iteoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''
"""
string = '''
http://www.iteoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''
domains = re.findall(r'https?://([\w.-]+)', string)
print(domains)


"""
计算一个字符串中所有的数字的和

比如:  string = 'hello90abc 78sjh12.5'
结果:  180.5 (90 + 78 + 12.5)
"""
string = 'hello90abc 78sjh12.5'
res = re.findall(r'\d+\.?\d*', string)
total = 0.0

for i in res:
    total += float(i)
print(total)


