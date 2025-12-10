'''
문제: https://www.acmicpc.net/problem/13549
접근: 숨바꼭질2와 같은 풀이볍, 순간이동 시에 시간이 다르다는 것만 계산하면 됨

시간복잡도: O(N)
'''

from collections import deque

def plus(num):
  return num + 1, 1

def minus(num):
  return num - 1, 1

def double(num):
  return num * 2, 0

N, K = map(int, input().split())

dp = [21e8] * 100001

dq = deque([(N, 0)])

moves = [plus, minus, double]

while dq:
  cur_loc, cur_move = dq.popleft()
  dp[cur_loc] = min(dp[cur_loc], cur_move)

  for move in moves:
    next_loc, time = move(cur_loc)

    if next_loc < 0 or next_loc >= len(dp):
      continue
    
    if dp[next_loc] <= cur_move + time:
      continue

    dq.append((next_loc, cur_move + time))

print(dp[K])
