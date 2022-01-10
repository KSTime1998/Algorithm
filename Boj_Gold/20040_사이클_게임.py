# 20040 - 사이클 게임 (Gold 4) - 유니온 파인드
import sys
N,M = map(int,sys.stdin.readline().split())
Possible = 0
connected = [i for i in range(N)]

def find(x):
  if connected[x] == x:
    return x
  else:
    return find(connected[x])

def union(X,Y):
  connected[max(X,Y)] = connected[min(X,Y)]

for m in range(M):
  s,e = map(int,sys.stdin.readline().split())
  if Possible == 0:
    S = find(s)
    E = find(e)
    if S == E:
      Possible = m+1
    else:
      union(S,E)

print(Possible)
