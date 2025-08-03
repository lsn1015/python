#### While loop statements #####

right = 1
while right <= 9:

    left = 1
    while left <= right:
        print(f"{left} x {right} = {left * right }", end="\t")
        left += 1
    print()

    right += 1


#### For loop statements #####

for right in range(1,10):
    for left in range(1,right+1):
        print(f'{left}x{right}={left * right}', end="  ")
    print()