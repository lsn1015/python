# text = "In 2026, Sunny will study Artificial Intelligence at KAIST! It's her dream goal."
#
# lst = text.split()
# print(f'1. ', lst)
# print(f'2. ', lst[::-1])
# l = [i for i in lst if i.isupper()]
# print(f'3. ', l)
# c = [c for c in lst if c.isdigit()]
# print(f'4. ', c)
# t = text.lower()
# print(t)
# import numpy as np
# lst = [8, 9, 0, 1, 7, 2]
#
# arr = np.array(lst)
# print(lst)
# print(arr)
# print('_' * 30)
# print(lst[4])
# print(arr[4])
import string
from collections import Counter

text = """
In 2026, Sunny will study Artificial Intelligence at KAIST. She believes that AI will shape the future of humanity. 
Her journey began in 2024, when she first discovered Python and fell in love with coding.
"""

# 1. 清洗 + 分词
text = text.lower()
words = [word.strip(string.punctuation)for word in text.split()]
text = text.lower()
words = [word.strip(string.punctuation) for word in text.split()]
print("1.", words)

# 2. 词频统计
counter = Counter(words)
counter = Counter(words)
print("2.", counter.items())

# 3. 最长最短单词（去掉数字）
pure_words = [w for w in words if w.isalpha()]
max_len = max(len(w) for w in pure_words)
min_len = min(len(w) for w in pure_words)
print(f"3. 最长单词: {[w for w in pure_words if len(w) == max_len]}，长度 {max_len}")
print(f"3. 最短单词: {[w for w in pure_words if len(w) == min_len]}，长度 {min_len}")

# 4. 出现超过1次
print("4.", [word for word, count in counter.items() if count > 1])

# 5. 以s开头
print("5.", [w for w in pure_words if w.startswith('s')])


# text = """
# In 2026, Sunny will study Artificial Intelligence at KAIST. She believes that AI will shape the future of humanity.
# Her journey began in 2024, when she first discovered Python and fell in love with coding.
# """
import string


# t = text.lower()
# lst = t.split()
# cleaned = [word.strip(',.!?\n') for word in lst]
# clean = [word.strip(string.punctuation) for word in lst]
# print('1,', cleaned)
# print('1,', clean)
#
# d = {}
# for i in lst:
#     nums = lst.count(i)
#     d[i] = nums
# print('2.', d.items())
#
# n = 0
# for i in lst:
#     if i.isalpha():
#         if len(i) > n:
#             n = len(i)
#             l = []
#             l.append(i)
# print(f'3.这句话最长的单词是{l},有{n}位。')
#
# x = 5
# for j in lst:
#     if len(j) > 0:
#         if len(j) < x:
#             x = len(j)
#             y = []
#             y.append(j)
#
# print(f'3.这句话最短的单词是{y}长度{x}')
#
# for i in lst:
#      if lst.count(i) > 1:
#          print(i)
#
# for i in lst:
#     if i.startswith(('s'),):
#         print(i)

