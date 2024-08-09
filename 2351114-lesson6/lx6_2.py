#2351114 朱俊泽 大数据科学与技术
'''
你正在图书馆坐着，一位陌生美女主动过来和你搭讪，并要求和你一起玩个数学游戏。
美女提议：“让我们各自亮出硬币的一面，或正或反。如果我们都是正面，那么我给你3元，
如果我们都是反面，我给你1元，剩下的情况你给我2元就可以了。”
自学掌握纳什均衡解决图书馆硬币博弈的理论
假设你是jack,美女是rose,rose将根据纳什均衡理论采取最佳策略。
请为jack选一个策略，编程实现jack,rose 100万次pk，输出最终两人的输赢情况。
'''

import random

# 定义游戏规则
def play_game(jack_choice, rose_prob):
    rose_choice = random.choices([0, 1], weights=[1 - rose_prob, rose_prob])[0]
    if jack_choice == 0 and rose_choice == 0:  # 都是正面
        return 3, -3
    elif jack_choice == 1 and rose_choice == 1:  # 都是反面
        return 1, -1
    else:  # 一正一反
        return -2, 2

# 计算Rose的纳什均衡策略
def calculate_nash_equilibrium():
    # 设Rose选择正面的概率为p，反面的概率为1-p
    # 计算Jack选择正面和反面时的期望收益
    # Jack选择正面时的期望收益：3p + (-2)(1-p) = 3p - 2 + 2p = 5p - 2
    # Jack选择反面时的期望收益：(-2)p + 1(1-p) = -2p + 1 - p = 1 - 3p
    # 令两者相等，求解p
    p = (1 + 2) / (5 + 3)
    return p

# 模拟100万次对局
def simulate_games(num_games, rose_prob):
    jack_total = 0
    rose_total = 0
    for _ in range(num_games):
        jack_choice = random.choice([0, 1])  # Jack随机选择正面或反面
        jack_result, rose_result = play_game(jack_choice, rose_prob)
        jack_total += jack_result
        rose_total += rose_result
    return jack_total, rose_total

# 主函数
def main():
    num_games = 1000000
    rose_prob = calculate_nash_equilibrium()
    jack_total, rose_total = simulate_games(num_games, rose_prob)
    print(f"Jack的总收益: {jack_total}")
    print(f"Rose的总收益: {rose_total}")

if __name__ == "__main__":
    main()
