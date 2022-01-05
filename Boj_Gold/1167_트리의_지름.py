# 1167 - 트리의 지름 (Gold 3) 
import sys
V = int(sys.stdin.readline())
node = [{} for _ in range(V+1)]
for _ in range(V):
  Line = list(map(int,sys.stdin.readline().split()))
  s = Line[0]
  for i in range(1,len(Line),2):
    e = Line[i]
    if e != -1:
      if e in node[s]:
        node[s][e] = min(node[s][e],Line[i+1])
      else:
        node[s][e] = Line[i+1]

def dfs(S):
  distance = [-1] * (V+1)
  distance[0] = distance[S] = 0
  farpoint = [S,0]
  visit = [S]
  left = 0
  right = 1
  while right > left:
    for i in range(left,right):
      parent = visit[i]
      for child in node[parent].keys():
        if distance[child] < 0:
          distance[child] = distance[parent] + node[parent][child]
          visit.append(child)
          if distance[child] > farpoint[1]:
            farpoint = [child,distance[child]]
    left = right
    right = len(visit)

  return farpoint

print(dfs(dfs(1)[0])[1])
