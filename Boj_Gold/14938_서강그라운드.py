# 14938 - 서강그라운드 (Gold 4)
import sys
import heapq
n,m,r = map(int,sys.stdin.readline().split())
items = [0] + list(map(int,sys.stdin.readline().split()))
road = [{} for _ in range(n+1)]
for _ in range(r):
  s,e,v = map(int,sys.stdin.readline().split())
  road[s][e] = road[e][s] = v

ans = 0
for s in range(1,n+1):
  checked = set()
  length = [1000] * (n+1)
  visit = [(0, s)]
  length[s] = 0
  while visit:
    start = visit[0][1]
    heapq.heappop(visit)
    if start not in checked:
      for i in road[start].keys():
        length[i] = min(length[i],length[start] + road[start][i])
        heapq.heappush(visit,(length[i],i))
      checked.add(start)
  a = 0
  for i in range(1,n+1):
    if length[i] <= m:
      a += items[i]
  ans = max(ans,a)

print(ans)
