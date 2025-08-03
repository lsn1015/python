
"""
已知字典 d = {'a': 100, (): '9', 8.1: 'b', True: 3+4j}, 计算键和值中所有数字类型的数据之和

即: 100 + 8.1 + True + 3+4j = 112.1+4j
"""

d = {'a': 100, (): '9', 8.1: 'b', True: 3+4j}
lst = list(d.items())
total = 0 + 0j
numbers = []

for var1, var2 in lst:
    t = (int, float, complex, bool)
    if type(var1) in t:
        total += var1
        numbers.append(var1)
    if type(var2) in t:
        total += var2
        numbers.append(var2)

result = '+'.join(str(num) for num in numbers)
print(f'{result} = {total}')
