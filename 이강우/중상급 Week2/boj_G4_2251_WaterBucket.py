'''
문제: https://www.acmicpc.net/problem/2251
접근: 가능한 모든 경우의 수를 고려해보자 > bfs? dfs? 사용 가능
A, B, C에 서로 물을 붓는 경우의 수를 고려한 후(이중 for), 
A가 비어있는 경우에 C에 담긴 물을 확인

시간복잡도: 
'''

from collections import deque

A, B, C = map(int, input().split())

# A, B의 물의 양 조합을 기록할 visited
comb = set((0, 0))

dq = deque([(0, 0)])

# 가능한 물의 양이 겹칠 수 있으니, list 말고 set
result = set()

while dq:
  a, b = dq.popleft()
  # C에 담긴 물의 양은 이렇게 계산 가능
  c = C - a - b

  if not a:
    result.add(c)

  cur_water = [a, b, c]
  limits = [A, B, C]

  # a, b, c가 서로 옮기는 경우의 수 = 3 * 3 - 3(자기 자신)
  for i in range(3):
    for j in range(3):
      if i == j:
        continue
    
      pour = min(cur_water[i], limits[j] - cur_water[j])

      # 만약 물을 따라서 옮길 수 있다면
      if pour > 0:
        next_water = cur_water[:]

        next_water[i] -= pour
        next_water[j] += pour

        # a, b는 리스트의 0, 1번째
        new_a, new_b = next_water[0], next_water[1]

        if (new_a, new_b) not in comb:
          comb.add((new_a, new_b))
          dq.append((new_a, new_b))


print(*sorted(list(result)))