import time
import random
import sys
import os


def animated_thinking(num):
    """动态显示 '思考中...'，模拟加载动画"""
    for _ in range(num):  # 控制动画循环次数
        for dots in [" ", ".", "..", "..."]:
            sys.stdout.write(f"\r思考中{dots}  ")  # \r 让文本回到行首
            sys.stdout.flush()
            time.sleep(0.25)
    sys.stdout.write("\r" + " " * 20 + "\r")  # 清除文本
    sys.stdout.flush()


def main():
    while True:
        user_input = input("向 deepseek 提问吧:\n")
        num = random.randint(10, 30)
        animated_thinking(num)  # 等待动画
        print("服务器繁忙，请稍后重试。")


if __name__ == '__main__':
    main()
