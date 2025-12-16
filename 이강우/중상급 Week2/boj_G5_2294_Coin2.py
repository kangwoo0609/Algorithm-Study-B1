'''
문제: https://www.acmicpc.net/problem/2294
접근:

시간복잡도:
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
dp = [21e8] * (k + 1)
dp[0] = 0

for _ in range(n):
  coins.append(int(input()))

for coin in coins:
  for i in range(coin, k + 1):
    # 어차피 동전 개수 하나 더하는 게 그 다음 경우의 수니까?
    dp[i] = min(dp[i - coin] + 1, dp[i])

print(dp[k]) if dp[k] != 21e8 else print(-1)