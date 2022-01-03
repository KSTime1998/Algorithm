# 1865 - 웜홀 (Gold 3) - 벨만-포드 알고리즘
import sys

def search(n,d,r):
  d[1] = 0
  for i in range(1,n+1):
    for start in range(1,n+1):
      for next, time in r[start]:
        if d[next] > d[start] + time:
          d[next] = d[start] + time
          if i == n:
            return False
  return True

for tc in range(int(sys.stdin.readline())):
  N,M,W = map(int,sys.stdin.readline().split())
  road = [[]*(N+1) for _ in range(N+1)]
  distance = [100000001]*(N+1)
  for _ in range(M):
    s,e,t = map(int,sys.stdin.readline().split())
    road[e].append([s,t])
    road[s].append([e,t])
  for _ in range(W):
    s,e,t = map(int,sys.stdin.readline().split())
    road[s].append([e,-t])

  if search(N,distance,road):
    print('NO')
  else:
    print('YES')
