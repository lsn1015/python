# text = "Sunny is learning AI in 2025 and will go to KAIST!"
#
# # 1. 提取字符串中 "learning" 这个词
# # 2. 提取年份（数字）
# # 3. 把整句话转为大写输出
# # 4. 判断 "KAIST" 是否出现在字符串中（True / False）
# # 5. 把字符串按空格切分后，取出最后一个单词（去除标点）
# lst = text.split()
# print('1.',text[9:18])
# print('1.',lst[2])
# print('2.', [i for i in lst if i.isdigit()])
# print('2.',lst[5])
# print('3',text.upper())
# print('4','KAIST' in text)
# print('5',lst[-1].strip('!'))
#
#
# nums = [12, 45, 67, 23, 89, 90, 34, 22]
#
# # 1. 取出前三个元素
# # 2. 取出倒数三个元素
# # 3. 提取所有大于50的数字，放入新列表
# # 4. 判断列表中是否存在 23
# # 5. 将原列表倒序排列后输出（不要用 reverse()）
#
# print('1.', nums[:3:])
# print('1.', nums[0], nums[1], nums[2])
# print('2.', nums[-1], nums[-2], nums[-3])
# print('2.', nums[-3::])
# new_nums = [i for i in nums if i > 50]
# print('3.', new_nums)
# print('4.', 23 in nums)
# print('5.', nums[::-1])

# scores = [55, 80, 90, 45, 60, 30, 95, 67]

# 1. 统计有多少人及格（>=60）
# 2. 找出不及格分数，并组成一个新列表
# 3. 求所有成绩的平均分（保留两位小数）
# 4. 找出成绩中的最高分与最低分
# n = 0
# for i in scores:
#     if i >= 60:
#         n = n + 1
# print(f'1.',[i for i in scores if i >= 60])
# print(f'1.{n} people pass')
# lst = [i for i in scores if i < 60]
# print(f'2.', lst)
# print(f'3:')
# nums = 0
# t = 0
# for i in scores:
#     nums += i
#     t += 1
# print(f'平均分为：{nums / t}')
# avg = round(sum(scores) / len(scores),2)
# print(f'平均分为：{avg}')
# print(f'4:', max(scores))
# #
# max_score = scores[0]
# for score in scores:
#     if score > max_score:
#         max_score = score
# print('最高分是：', max_score)
#
# mini_score = scores[0]
# for i in scores:
#     if i < mini_score:
#         mini_score = i
# print('最低分是：', mini_score)
#
# def find_max(nums):
#     m = nums[0]
#     for i in nums:
#         if i > m:
#             m = i
#     return m
# h = find_max(scores)
# print(f'highest score is:', h)
# #1
# nums = [12, 56, 32, 78, 5, 89, 34]
# max_nums = nums[0]
# for i in nums:
#     if i > max_nums:
#         max_nums = i
# print(f'max number is:', max_nums)
#
# mini_nums = nums[0]
# for i in nums:
#     if i < mini_nums:
#         mini_nums = i
# print(f'mini number is:', mini_nums)
# #2
# nums = [20, 30, 50, 70, 90]
# total = 0
# for i in nums:
#     total += i
# print(f'total is:', total)
# print(f'average is:', total / len(nums))
# #3
# nums = [10, 45, 67, 89, 34, 89, 22]
# max_j = 1
# for i in range(len(nums)):
#     if nums[i] > nums[max_j]:
#         max_j = i
#         print(max_j)
# print(nums[2])
# #4
# nums = [10, 15, 22, 37, 40, 55, 66, 77, 88, 99]
# even = 0
# odd = 0
#
# for i in nums:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f'偶数个数：',even)
# print(f'奇数个数：',odd)
#
# #5
# nums = [12, 35, 14, 65, 40, 70, 45]
# j = 1
# for i in range(len(nums)):
#     diff = nums[i] - nums[j]
#     if abs(diff) > 20:
#         print(f'差值为{abs(diff)}:{nums[i]},{nums[j]}')
#     j += 1

text = "Sunny will go to KAIST in 2026 and study Artificial Intelligence."

# 1. 找出所有的数字字符
# 2. 找出所有大写字母
# 3. 统计空格数量
# 4. 将所有单词倒序输出（即最后一个词在最前）
##1
for i in text:
    if i.isdigit():
        print(i)
lst = text.split()
for i in lst:
    if i.isdigit():
        print(i)
##2
caps = [i for i in text if i.isupper()]
print(caps)

##3
print(text.find(' ',0))
##4

print('单词倒序：', ''.join(lst[::-1]))
for i, word in enumerate(lst[::-1],1):
    print(f'{i}.{word}')