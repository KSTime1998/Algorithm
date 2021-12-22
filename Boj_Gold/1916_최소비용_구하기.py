# 1916 - 최소비용 구하기 (Gold 5)
import sys
import heapq
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
node = [{} for _ in range(N+1)]
for _ in range(M):
  s,e,v = map(int,sys.stdin.readline().split())
  if e not in node[s]:
    node[s][e] = v
  else:
    node[s][e] = min(node[s][e],v)
S,E = map(int,sys.stdin.readline().split())

value = [1000000001] * (N+1)
value[S] = 0
checked = set()
visit = [(0,S)]
while len(visit) > 0:
  v = visit[0][1]
  heapq.heappop(visit)
  if v in checked:
    continue
  for i in node[v].keys():
    value[i] = min(value[i], value[v] + node[v][i])
    heapq.heappush(visit,(value[i],i))
  checked.add(v)

print(value[E])
