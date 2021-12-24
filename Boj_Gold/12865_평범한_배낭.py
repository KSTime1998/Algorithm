# 12865 - 평범한 배낭 (Gold 5)
import sys
N,K = map(int,sys.stdin.readline().split())
things = []
for _ in range(N):
  things.append(list(map(int,sys.stdin.readline().split())))
maxvalue = [[0] * (K+1) for _ in range(N)]

for i in range(N):
  w = things[i][0]
  v = things[i][1]
  for j in range(1,K+1):
    if j < w:
      maxvalue[i][j] = maxvalue[i-1][j]
    else:
      maxvalue[i][j] = max(maxvalue[i-1][j], maxvalue[i-1][j-w] + v) 
print(maxvalue[-1][-1])
