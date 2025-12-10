'''
문제: https://www.acmicpc.net/problem/12851
접근: 움직일 수 있는 게, +1, -1, *2
이 움직임을 bfs로 돌면서, dp에 담아서 최소 움직임을 구하면 될 것이라고 생각 했음

시간복잡도: dp에 담길 수 있는 길이만큼 > O(N)
'''

from collections import deque

def plus(num):
  return num + 1

def minus(num):
  return num - 1

def double(num):
  return num * 2

N, K = map(int, input().split())

dp = [21e8] * 100001

dq = deque([(N, 0)])

moves = [plus, minus, double]

options = 0

while dq:
  cur_loc, cur_move = dq.popleft()
  if cur_loc == K:
    if cur_move < dp[K]:
      options = 1
      dp[K] = cur_move
    elif cur_move == dp[K]:
      options += 1
  else:
    dp[cur_loc] = min(dp[cur_loc], cur_move)

  for move in moves:
    next_loc = move(cur_loc)

    if next_loc < 0 or next_loc >= len(dp):
      continue
    
    if dp[next_loc] < cur_move + 1:
      continue

    dq.append((next_loc, cur_move + 1))

print(dp[K])
print(options)