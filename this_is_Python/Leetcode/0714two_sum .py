def twosum(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] +num[j] == target:
                return i, j

print(twosum([1, 2, 3], 3))
print(twosum([2, 5, 7], 9))