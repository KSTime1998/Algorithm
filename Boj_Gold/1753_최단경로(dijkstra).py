# 1753 - 최단경로 (Gold 5) - 다익스트라 / 왜 더 느림?
import sys
import heapq
V,E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())

node = [{} for _ in range(V+1)]
value = [1000000000]*(V+1)
value[K] = 0

for _ in range(E):
  u,v,t = map(int,sys.stdin.readline().split())
  if v not in node[u]:
    node[u][v] = t
  else:
    node[u][v] = min(t,node[u][v])

visit = [(0,K)]
checked = set()
while len(visit) > 0:
  location = visit[0][1]
  heapq.heappop(visit)
  if location in checked:
    continue
  for pos in node[location].keys():
    value[pos] = min(value[pos], node[location][pos] + value[location])
    heapq.heappush(visit,(value[pos],pos))
  checked.add(location)

for i in range(1,V+1):
  if value[i] == 1000000000:
    value[i] = 'INF'
print('\n'.join(map(str,value[1:])))
