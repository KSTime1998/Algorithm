# 1043 - 거짓말 (Gold 4)
import sys
N,M = map(int,sys.stdin.readline().split())
true = list(map(int,sys.stdin.readline().split()))[1:]
parties = [list(map(int,sys.stdin.readline().split()))[1:] for _ in range(M)]

node = [set() for _ in range(N+1)]
for party in parties:
  for i in range(len(party)):
    for j in range(i+1,len(party)):
      I = party[i]
      J = party[j]
      node[I].add(J)
      node[J].add(I)

left = 0
right = len(true)
visited = [0] * (N+1)
for t in true:
  visited[t] = 1
while left < right:
  for i in range(left,right):
    parent = true[i]
    for child in node[parent]:
      if visited[child] == 0:
        visited[child] = 1
        true.append(child)
  left = right
  right = len(true)

cnt = 0
for party in parties:
  possible = True
  for p in party:
    if visited[p] == 1:
      possible = False
      break
  if possible:
    cnt += 1

print(cnt)
