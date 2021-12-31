# 11779 - 최소비용 구하기 2 (Gold 3)
import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
node = [{} for _ in range(n+1)]
for _ in range(m):
  s,e,v = map(int,sys.stdin.readline().split())
  if e in node[s]:
    node[s][e] = min(node[s][e],v)
  else:
    node[s][e] = v
start,end = map(int,sys.stdin.readline().split())

checked = [0]*(n+1)
visit = [[0,start]]
value = [10000000001]*(n+1)
parent = [start]*(n+1)
value[start] = 0
while visit:
  s = visit[0][1]
  heapq.heappop(visit)
  if checked[s] != 1:
    for next in node[s].keys():
      if value[next] > value[s]+node[s][next]:
        value[next] = value[s]+node[s][next]
        parent[next] = s
      heapq.heappush(visit,[value[next],next])
    checked[s] = 1

path = [end]
def findpath(child):
  p = parent[child]
  path.append(p)
  if p != start:
    findpath(parent[child])

findpath(end)

print(value[end])
if start == end:
  print(1,1,sep='\n')
else:
  print(len(path))
  print(' '.join(map(str,path[::-1])))
