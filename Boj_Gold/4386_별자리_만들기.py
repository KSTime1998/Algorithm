# 4386 - 별자리 만들기 (Gold 4) - 크루스칼 알고리즘(최소 스패닝 트리)
import sys

def parent(x):
  if connected[x] == x:
    return x
  return parent(connected[x])

def union(p1,p2):
  connected[max(p1,p2)] = connected[min(p1,p2)]

N = int(sys.stdin.readline())
node = []
coords = []
for i in range(N):
  x,y = map(float,sys.stdin.readline().split())
  for n in range(len(coords)):
    X,Y = coords[n][0],coords[n][1]
    node.append([n,i,((x-X)**2 + (y-Y)**2)**(1/2)])
  coords.append([x,y])

ans = 0
node.sort(key = lambda x : x[2])
connected = [i for i in range(N+1)]
for star1,star2,d in node:
  S1 = parent(star1)
  S2 = parent(star2)
  if S1 != S2:
    ans += d
    union(S1,S2)

print(round(ans,2))
