# 1504 - 특정한 최단 경로 (Gold 4)
import sys
import heapq
N,E = map(int,sys.stdin.readline().split())
node = [{} for _ in range(N+1)]
for _ in range(E):
  a,b,c = map(int,sys.stdin.readline().split())
  if b in node[a]:
    node[a][b] = min(node[a][b],c)
    node[b][a] = node[a][b]
  else:
    node[a][b] = node[b][a] = c
v1,v2 = map(int,sys.stdin.readline().split())
route1 = [1,v1,v2,N]
route2 = [1,v2,v1,N]

def djikstra(start,end):
  global Possible,a
  checked = set()
  visit = [(0,start)]
  value = [200000001] * (N+1)
  value[start] = 0
  while visit:
    if end in checked:
      break
    s = visit[0][1]
    heapq.heappop(visit)
    if s not in checked:
      for next in node[s].keys():
        value[next] = min(value[next], value[s] + node[s][next])
        heapq.heappush(visit, (value[next],next))
      checked.add(s)
  if value[end] == 200000001:
    Possible = False
  else:
    a += value[end]

ans = 100000000
Possible = True
a = 0
for i in range(3):
  djikstra(route1[i],route1[i+1])
  if not Possible:
    break
if Possible:
  ans = a

Possible = True
a = 0
for i in range(3):
  djikstra(route2[i],route2[i+1])
  if not Possible:
    break
if Possible:
  ans = min(ans,a)

if ans == 100000000:
  print(-1)
else:
  print(ans)
