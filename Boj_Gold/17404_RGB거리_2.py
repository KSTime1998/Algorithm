# 17404 - RGB거리 2 (Gold 4)
import sys
N = int(sys.stdin.readline())
RGB = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = 1000001

def firstcolor(color):
  global ans
  R = [0]*N
  G = [0]*N
  B = [0]*N
  if color == 0:
    R[0] = RGB[0][0]
    G[0] = B[0] = 1000001

  elif color == 1:
    G[0] = RGB[0][1]
    R[0] = B[0] = 1000001

  elif color == 2:
    B[0] = RGB[0][2]
    G[0] = R[0] = 1000001

  for n in range(1,N):
    R[n] = min(G[n-1],B[n-1])+RGB[n][0]
    G[n] = min(R[n-1],B[n-1])+RGB[n][1]
    B[n] = min(R[n-1],G[n-1])+RGB[n][2]

  if color == 0:
    ans = min(ans,G[n],B[n])
  elif color == 1:
    ans = min(ans,R[n],B[n])
  elif color == 2:
    ans = min(ans,R[n],G[n])

firstcolor(0)
firstcolor(1)
firstcolor(2)
print(ans)
