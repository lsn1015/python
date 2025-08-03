
### Rock Paper Scissors Game 3.0 ###

import random

# 映射手势到数值
d = {'Rock': 0, 'Scissors': 1, 'Paper': 2}
choices = list(d)

# 记录分数
player_score = 0
computer_score = 0

print("🎮 Rock–Paper–Scissors Game: Best of 5 (先赢3局者获胜)\n")

# 游戏循环
count = 0
while player_score < 3 and computer_score < 3:
    # 玩家输入
    player = input("Rock, Paper or Scissors? ").strip().capitalize()
    count += 1
    if count == 5:
        break

    # 输入校验
    if player not in d:
        print("⚠️ 请输入正确的手势：Rock / Paper / Scissors\n")
        continue

    # 电脑随机选择
    computer = random.choice(choices)

    # 显示双方选择
    print(f"🧠 Computer: {computer} | 🧍 Player: {player}")

    # 数值映射
    c_val = d[computer]
    p_val = d[player]

    # 判断胜负
    if p_val - c_val in (-1, 2):
        player_score += 1
        print("✅ Player wins this round!\n")
    elif p_val == c_val:
        print("🤝 Tie! No one scores.\n")
    else:
        computer_score += 1
        print("❌ Computer wins this round!\n")

    # 显示当前比分
    print(f"🏅 Score => Player: {player_score} | Computer: {computer_score}\n")

# 结束语
if player_score == 3:
    print("🎉 Congrats Sunny! You win the game!")
else:
    print("😈 Computer wins the game! Better luck next time!")