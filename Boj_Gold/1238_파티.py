# 1238 - 파티 (Gold 3)
import sys
import heapq

def findway(start,distance):
  visit = [[0,start]]
  checked = [0]*(N+1)
  distance[start] = 0
  while visit:
    s = visit[0][1]
    heapq.heappop(visit)
    if checked[s] == 0:
      for next in road[s].keys():
        if distance[next] > distance[s] + road[s][next]:
          distance[next] = distance[s] + road[s][next]
          heapq.heappush(visit,(distance[next],next))
      checked[s] = 1

N,M,X = map(int,sys.stdin.readline().split())
road = [{} for _ in range(N+1)]
for _ in range(M):
  s,e,t = map(int,sys.stdin.readline().split())
  road[s][e] = t

maxtime = 0
gohome = [10000001]*(N+1)
findway(X,gohome)
for i in range(1,N+1):
  if i != X:
    goparty = [10000001]*(N+1)
    findway(i,goparty)
    maxtime = max(maxtime, goparty[X] + gohome[i])

print(maxtime)
