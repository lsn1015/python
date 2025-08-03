# scores = [45, 88, 72, 50, 91, 63]
# for i in scores:
#     if i >= 60:
#         print(i)
# #2
# s = "Sunny would be hard study in AI course in 2025, and go to Kaist for study!"
#
# for i in s:
#     if i.isdigit():
#         print(i)
#
# #3
#
# for i in range(1,6):
#     print('*' * i)

#字符串切片
text = "KAIST is my dream school"
t = text.split()
#1
print(t[0])
print(t[-5])
#2
print(t[3])
print(t[-2])
#3
print(t[-1])
print(t[4])
#列表切片与元素提取
nums = [10, 20, 30, 40, 50, 60, 70]
#1
n = (nums[0], nums[1], nums[2])
print(n)
n = nums[0:3:1]
print(n)
#2
n = (nums[2], nums[3], nums[4])
print(n)
n = nums[2:5:1]
print(n)
#3
n = nums[::-1]
print(n)
n = nums.reverse()
print(nums)
#4
n = nums[::2]
print(n)
#集合的提取与去重理解
items = [1, 2, 2, 3, 4, 4, 5, 1, 6]
#1
i = set(items)
print(i)
#2
print(3 in i)
#3
s = list(i)
print(s)
print(sorted(s))


# 字符串切片
text = "KAIST is my dream school"
t = text.split()
print("1.", t[0])        # KAIST
print("2.", t[3])        # dream
print("3.", t[-1])       # school

# 列表切片
nums = [10, 20, 30, 40, 50, 60, 70]
print("4.", nums[:3])    # [10, 20, 30]
print("5.", nums[2:5])   # [30, 40, 50]
print("6.", nums[::-1])  # [70, 60, 50, 40, 30, 20, 10]
print("7.", nums[::2])   # [10, 30, 50, 70]

# 集合去重与处理
items = [1, 2, 2, 3, 4, 4, 5, 1, 6]
i = set(items)
print("8.", i)
print("9.", 3 in i)      # True
i.discard(3)
s = list(i)
print("10.", sorted(s))  # [1, 2, 4, 5, 6]