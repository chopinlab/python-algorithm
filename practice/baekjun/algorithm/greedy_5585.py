"""
greedy
https://www.acmicpc.net/problem/5585
거스름돈
"""

"""
380   # 4
1     # 15 
"""

change = 1000 - int(input())
count = 0
coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    count += change // coin
    change %= coin

print(count)








