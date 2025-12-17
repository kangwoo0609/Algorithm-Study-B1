'''
문제: https://www.acmicpc.net/problem/9370
접근: s에서 출발하여 g -> h 혹은 h -> g의 경로를 거쳐 최단 거리로 목적지에 간다.
임의의 위치로 가는데 적용된 가중치와 s-g-h, s-h-g 경로를 지난 가중치가 하나라도 일치하면,
그 임의의 위치는 목적지 후보가 될 수 있다.

시간복잡도:
'''

import sys
input = sys.stdin.readline
import heapq

def dijkstra(start, n, arr):
  distances = [21e8] * (n + 1)
  distances[start] = 0
  hq = []
  heapq.heappush(hq, (0, start))

  while hq:
    dist, now = heapq.heappop(hq)

    if dist > distances[now]:
      continue

    for node, cost in arr[now]:
      if cost + dist >= distances[node]:
        continue
      distances[node] = cost + dist
      heapq.heappush(hq, (cost + dist, node))

  return distances

T = int(input())
for _ in range(T):
  n, m, t = map(int, input().split())
  s, g, h = map(int, input().split())

  arr = [[] for _ in range(n + 1)]

  path_gh = 0
  for _ in range(m):
    a, b, d = map(int, input().split())
    arr[a].append((b, d))
    arr[b].append((a, d))

    if (a == g and b == h) or (a == h and b == g):
      path_gh += d

  candidates = []
  for _ in range(t):
    candidates.append(int(input()))

  from_s = dijkstra(s, n, arr)
  from_g = dijkstra(g, n, arr)
  from_h = dijkstra(h, n, arr)

  result = []
  for candidate in candidates:
    shortest = from_s[candidate]

    through_gh = from_s[g] + path_gh + from_h[candidate]
    through_hg = from_s[h] + path_gh + from_g[candidate]

    if shortest != 21e8 and shortest == min(through_gh, through_hg):
      result.append(candidate)

  result.sort()
  print(*result)