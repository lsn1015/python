
'''综合应用
编写一个简单的猜数字游戏：

程序随机生成1-100之间的数字

用户有5次猜测机会

每次猜测后提示"大了"或"小了"

猜中后显示"恭喜！"并结束游戏

用完机会显示正确答案'''

import random
print('Welcome to the Number Guessing Game!')
print("I've thought of a number between 1 and 100. You have 5 attempts to guess it.")

target = random.randint(1, 100)
attempts = 5

for attempt in range(1, attempts + 1):
    while True:
        guess = input(f'Attempt{attempt}, enter your guess(1-100): ').strip()
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 100:
                break
            else:
                print('please enter a number between 1 and 100!')
        else:
            print('please enter a valid number!')

    if guess < target:
        print('Too low!')
    elif guess > target:
        print('Too high!')
    else:
        print(f'Congratulations! You guessed the correct number{target} in {attempt} attempts!')
        break
else:
    print(f'Sorry, you didn\'t guess the number in 5 attempts. The correct answer was {target}.')