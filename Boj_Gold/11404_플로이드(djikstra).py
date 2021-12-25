# 11404 - 플로이드 (Gold 4) - 다익스트라
import sys
import heapq
nm = [int(sys.stdin.readline()) for _ in range(2)]
n = nm[0]
node = [{} for _ in range(n+1)]
for _ in range(nm[1]):
  a,b,c = map(int,sys.stdin.readline().split())
  if b in node[a]:
    node[a][b] = min(node[a][b],c)
  else:
    node[a][b] = c

for i in range(1,n+1):
  cost = [1000000001] * (n+1)
  cost[i] = 0
  checked = set()
  visit = [(0,i)]
  while visit:
    start = visit[0][1]
    heapq.heappop(visit)
    if start not in checked:
      for next in node[start].keys():
        cost[next] = min(cost[next], cost[start] + node[start][next])
        heapq.heappush(visit, (cost[next],next))
      checked.add(start)

  for i in range(n+1):
    if cost[i] == 1000000001:
      cost[i] = 0
  print(' '.join(map(str,cost[1:])))
