from collections import Counter
import string
students = [
    ("Sunny", 88),
    ("Alice", 95),
    ("Bob", 67),
    ("David", 76),
]
s = sorted(students, key=lambda x : x[1], reverse=True)
print(s)
students = [
    ("Sunny", 88),
    ("Alice", 95),
    ("Bob", 67),
    ("David", 76),
]
s = sorted(students, key=lambda x : len(x[0]))
print(s)
text = "Sunny loves Python and AI. Sunny codes Python every day. AI is her dream."
text = text.lower()
clean = [c.strip(string.punctuation) for c in text.split()]
counter = Counter(clean)
top3 = sorted(counter.items(), key=lambda x:x[1], reverse=True)[:3]
print(top3)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = [c for c in nums if c % 2 == 0]
print(even_nums)
squared = [i ** 2 for i in nums]
print(squared)
e_squared = [i ** 2 for i in even_nums]
print(e_squared)

nums = [10, 15, 22, 33, 40, 55, 60, 75, 80]

# 1. 用 if-else 推导式：将奇数变为 "odd"，偶数保留原值，生成一个新列表
# 2. 用嵌套推导式：展开下面的二维列表 matrix
matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
# 3. 用 lambda + filter + map：从 nums 中找出能被 5 整除的数，并计算它们的平方
odd1 = [c if c % 2 == 0 else 'odd' for c in nums]
print(odd1)
m = [j for i in matrix for j in i]
print(m)
n = list[map(lambda i : i**2, filter(lambda i : i % 5 == 0, nums))]
print(n)

""" ✅第 1 题：奇偶替换平方

给定一个整数列表 nums = [10, 15, 22, 33, 40, 55]，将奇数变成字符串 "odd"，偶数变成它的平方。

✨ 输出格式："""

[100, 'odd', 484, 'odd', 1600, 'odd']

n = [i ** 2 if i % 2 == 0 else 'odd' for i in nums]


"""✅ 第 2 题：取出大于50的平方结果（使用 filter + map + lambda）

仍用 nums = [10, 15, 22, 33, 40, 55]
	•	步骤1：先过滤出 > 20 的数
	•	步骤2：再对它们平方"""

"""✨ 输出格式："""

"""[484, 1089, 1600, 3025]"""

l = [list(map(lambda x: x**2, filter(lambda x: x > 50, nums)))]



"""✅ 第 3 题：嵌套列表展开 + 平方（综合推导式）

matrix = [[1, 2], [3, 4], [5, 6]]

输出每个元素的平方，用一行推导式写出

✨ 输出格式：[1, 4, 9, 16, 25, 36]"""

n = [j ** 2 for i in matrix for j in i]

"""✅ 字典推导式题目：

给定："""

words = ['study', 'sunny', 'ai', 'python']

"""创建一个字典，键为单词，值为该单词的长度
输出：{'study': 5, 'sunny': 5, 'ai': 2, 'python': 6}
"""

dic = [{i, len(i)} for i in words]
print(dic)

"""✅ 集合推导式题目：

从下列文本中找出不重复的以 “s” 开头的单词（不区分大小写）"""

text1 = "Sunny studies smart solutions and seeks scalable systems."

"""输出为一个集合（set），不包含标点，全部小写：{'sunny', 'studies', 'smart', 'solutions', 'seeks', 'scalable', 'systems'}"""


text2 = text1.lower()
clean = [word.strip(string.punctuation) for word in text2.split()]
s = [i for i in clean if i.startswith('s')]
print(set(s))

# 要求：
# 1. 清洗文本（转小写，去标点）
# 2. 找出所有以 s 开头、长度大于 5 的单词，组成列表
# 3. 输出每个单词对应的长度（dict）
# 4. 输出这些单词中最长的那个
text2 = "Python is simple and powerful. Sunny studies smart solutions and scalable systems."

text3 = text2.lower()
cleaned = [word.strip(string.punctuation) for word in text3.split()]
lst = [c for c in cleaned if c.startswith('s') and len(c) > 5]
print(lst)
d = {word:len(word) for word in lst}
print(d)
longest = max(lst, key=len)
print(longest)