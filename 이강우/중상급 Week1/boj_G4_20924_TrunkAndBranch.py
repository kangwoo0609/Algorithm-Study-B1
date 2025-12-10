'''
문제: https://www.acmicpc.net/problem/20924
접근: 기가 노드가 나올 때까지 trunk bfs, 기가 노드 이후에는 branch bfs
처음에는 branch를 dfs로 구현했는대, recursion error 떠서 그냥 bfs로 구현함

시간복잡도:
'''

import sys
input = sys.stdin.readline
from collections import deque

N, R = map(int, input().split())

tree = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
  a, b, d = map(int, input().split())
  # 단방향 아님 주의
  tree[a].append((b, d))
  tree[b].append((a, d))

# print(tree)

trunk = 0
branch = 0

# 루트 노듸는 1이 아니라 R부터
trunk_dq = deque([R])

while trunk_dq:
  cur_node = trunk_dq.popleft()
  visited[cur_node] = 1

  # 루트부터 기가노드일 경우
  if len(tree[R]) > 1:
    break

  # 일반 노드 대상으로 기가노드 여부 확인
  if len(tree[cur_node]) > 2 or not tree[cur_node]:
    break
  
  # bfs로 순회하면서 기둥의 길이 더해주기
  for next_node, new_dist in tree[cur_node]:
    # 트리를 양방향으로 받았기 때문에 가지치기
    if visited[next_node]:
      continue
    else:
      trunk += new_dist
      trunk_dq.append(next_node)


# 최대 가지 길이 구하기 시작
# 여기의 cur_node는 trunk 길이 구했을 때 마지막 노드
branch_dq = deque([(cur_node, 0)])

# 그냥 bfs로 돌면서 매 순간 최대 길이 비교해주기
# 만약 최장 길이 가지를 찾는 거였으면.. dijkstra?
while branch_dq:
  cur_node, dist = branch_dq.popleft()

  visited[cur_node] = 1
  branch = max(branch, dist)

  for next_node, new_dist in tree[cur_node]:
    if visited[next_node]:
      continue
    branch_dq.append((next_node, dist + new_dist))

print(trunk, branch)