
'''''列表操作
创建一个包含5种水果的列表，然后：

添加一种新水果

删除第二种水果

打印列表长度和排序后的列表

函数
编写一个函数，接受两个数字参数，返回它们的和与乘积（以元组形式返回）。'''

lst = ['apple', 'banana', 'pear', 'orange', 'watermelon']
lst.append('grapefruit')
lst.pop(1)
print(len(lst),sorted(lst))