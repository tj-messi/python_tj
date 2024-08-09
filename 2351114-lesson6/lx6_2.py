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

# 定义Rose和Jack的策略
rose_prob_heads = 3 / 8
jack_prob_heads = 1 / 8

# 初始化输赢计数
rose_earnings = 0
jack_earnings = 0

# 模拟100万次博弈
for _ in range(1000000):
    # 随机决定Rose和Jack的硬币结果
    rose_coin = random.random() < rose_prob_heads
    jack_coin = random.random() < jack_prob_heads

    # 根据硬币结果计算输赢
    if rose_coin and jack_coin:  # 都是正面
        jack_earnings += 3
        rose_earnings -=3
    elif not rose_coin and not jack_coin:  # 都是反面
        jack_earnings += 1
        rose_earnings -=1
    else:  # 一正一反
        rose_earnings += 2
        jack_earnings -=2

# 输出最终结果
print(f"Rose的最终收益: {rose_earnings}元")
print(f"Jack的最终收益: {jack_earnings}元")
