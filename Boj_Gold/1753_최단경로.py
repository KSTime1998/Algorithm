# 1753 - 최단경로 (Gold 5) - 왜 되지?
import sys
V,E = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())

node = [{} for _ in range(V+1)]
for _ in range(E):
  s,e,v = map(int,sys.stdin.readline().split())
  if e in node[s]:
    node[s][e] = min(v,node[s][e])
  else:
    node[s][e] = v

value = [0] * (V+1)

def modifying(X):
  for x in X:
    for c in node[x].keys():
      if value[c] != 0 and value[c] > value[x] + node[x][c]:
        value[c] = value[x] + node[x][c]
        modifying([c])

visit = [start]
left = 0
right = len(visit)
while right > left:
  modi = set()
  for i in range(left,right):
    point = visit[i]
    for j in node[point].keys():
      if value[j] == 0:
        value[j] = value[point] + node[point][j]
        visit.append(j)
      elif value[j] > value[point] + node[point][j]:
        value[j] = value[point] + node[point][j]
        if j not in modi:
          modi.add(j)
  modifying(modi)
  left = right
  right = len(visit)

for i in range(1,V+1):
  if value[i] == 0 and i != start:
      value[i] = 'INF'
value[start] = 0
print('\n'.join(map(str,value[1:])))
