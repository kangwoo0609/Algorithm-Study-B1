'''
문제: https://www.acmicpc.net/problem/13460
접근: N * M의 배열을 delta 활용하여 탐삭하는 bfs
구슬이 한 칸 씩이 아니라, 끝까지 굴러간다는 점이 좀 다른 부분이었다.
제미나이 만세

시간복잡도: O(4 ** 10 * max(N, M)) 이라고 합니다.
delta로 움직이는 방향 4, 최대 10번 움직임, N, M 길이만큼 벽까지 굴러감
'''

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

rx, ry, bx, by = 0, 0, 0, 0

maze = []

for i in range(N):
  temp = list(input().strip())
  maze.append(temp)
  for j in range(M):
    if temp[j] == 'R':
      rx, ry = i, j

    elif temp[j] == 'B':
      bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque([(rx, ry, bx, by, 0)])

visited = set([(rx, ry, bx, by)])


flag = False
while dq:
  nrx, nry, nbx, nby, cnt = dq.popleft()

  if cnt >= 10:
    flag = False
    break

  for i in range(4):
    mx, my = dx[i], dy[i]
    crx, cry, cbx, cby = nrx, nry, nbx, nby
    r_cnt = 0
    while maze[crx + mx][cry + my] != '#' and maze[crx][cry] != 'O':
      crx += mx
      cry += my
      r_cnt += 1

    b_cnt = 0
    while maze[cbx + mx][cby + my] != '#' and maze[cbx][cby] != 'O':
      cbx += mx
      cby += my
      b_cnt += 1

    if maze[cbx][cby] == 'O':
      continue

    if maze[crx][cry] == 'O':
      flag = True
      cnt += 1
      break

    if crx == cbx and cry == cby:
      if r_cnt > b_cnt:
        crx -= dx[i]
        cry -= dy[i]
      else:
        cbx -= dx[i]
        cby -= dy[i]

    if (crx, cry, cbx, cby) not in visited:
      visited.add((crx, cry, cbx, cby))
      dq.append((crx, cry, cbx, cby, cnt + 1))

  if flag:
    break

# print(cnt)
# print(flag)
if flag:
  print(cnt)
else:
  print(-1)