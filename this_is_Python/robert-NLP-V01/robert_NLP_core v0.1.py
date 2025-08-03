def respond_to_command(command):
    command = command.lower()

    if "打开灯" in command:
        return "好的，正在为你打开灯。💡"
    elif "我累了" in command:
        return "要不要我放点音乐给你放松一下？🎵"
    elif "天气" in command:
        return "今天天气晴朗，适合出门走走哦！☀️"
    elif "你好" in command:
        return "你好，我是你的AI小助手！🤖"
    elif "关窗户" in command:
        return "好的，正在为你关窗，你准备休息了吗？"
    else:
        return "抱歉，我还不太明白这个指令。可以换一种说法试试吗？"


# 示例运行
while True:
    user_input = input("你对机器人说：")
    if user_input.lower() in ["退出", "exit"]:
        print("机器人已休眠，再见～")
        break
    print("🤖 机器人回答：", respond_to_command(user_input))