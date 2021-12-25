# 1967 - 트리의 지름 (Gold 4) - 몰?루
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
node = [{} for _ in range(n+1)]

for _ in range(n-1):
  p,c,v = map(int,sys.stdin.readline().split())
  node[p][c] = v
  node[c][p] = v

def bfs(start,length):
  for next in node[start].keys():
    if visited[next] == 0:
      visited[next] = 1
      bfs(next,length+node[start][next])
      visited[next] = 0
  if diameter[0] < length:
    diameter[0] = length
    diameter[1] = start

diameter = [0,0]
visited = [0]*(n+1)
visited[1] = 1
bfs(1,0)

visited = [0]*(n+1)
visited[diameter[1]] = 1
bfs(diameter[1],0)
print(diameter[0])
