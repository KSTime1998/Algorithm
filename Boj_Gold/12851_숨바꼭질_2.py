# 12851 - 숨바꼭질 2 (Gold 5) - 반례 주의!
import sys

def push(x):
    if x == K:
      global cnt
      cnt += 1
    elif x <= 100000 and visited[x] == 0:
      visit.append(x)

N,K = map(int,sys.stdin.readline().split())
visited = [0] * (100001)
visit = [N]
left = T = cnt = 0
right = 1
while True:
  T += 1
  for i in range(left,right):
    v = visit[i]
    visited[v] = 1
    if v > 0 :
      push(v-1)
    if v < K :
      push(v+1)
      push(v*2)
  if cnt != 0:
    print(T,cnt,sep='\n')
    break
  left = right
  right = len(visit)
