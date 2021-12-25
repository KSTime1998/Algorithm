# 2096 - 내려가기 (Gold 4)
import sys
N = int(sys.stdin.readline())

maxdp = [[0,0,0] for _ in range(2)]
mindp = [[0,0,0] for _ in range(2)]
for i in range(N):
  a,b,c = map(int,sys.stdin.readline().split())
  maxdp[1][0] = max(maxdp[0][0],maxdp[0][1]) + a
  maxdp[1][1] = max(maxdp[0][0],maxdp[0][1],maxdp[0][2]) + b
  maxdp[1][2] = max(maxdp[0][1],maxdp[0][2]) + c
  mindp[1][0] = min(mindp[0][0],mindp[0][1]) + a
  mindp[1][1] = min(mindp[0][0],mindp[0][1],mindp[0][2]) + b
  mindp[1][2] = min(mindp[0][1],mindp[0][2]) + c
  for j in range(3):
    maxdp[0][j] = maxdp[1][j]
    mindp[0][j] = mindp[1][j]
print(max(maxdp[-1]),min(mindp[-1]),sep=' ')
