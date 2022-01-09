# 7573 - 고기잡이 (Gold 4) - 반례지옥
import sys
N,L,M = map(int,sys.stdin.readline().split())
fish = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]

def find(x1,y1,x2,y2):
  if x2 - x1 > N or y2 - y1 > N:
    return

  global ans
  cnt = 0
  if x1 < 0:
    x2 -= x1
    x1 = 0
  elif x2 > N:
    x1 -= x2 - N
    x2 = N

  if y1 < 0:
    y2 -= y1
    y1 = 0
  elif y2 > N - 1:
    y1 -= y2 - N
    y2 = N

  for x,y in fish:
    if x1 <= x <= x2 and y1 <= y <= y2:
      cnt += 1
  
  ans = max(ans,cnt)

ans = 1
L //= 2
N -= 1
for i in range(M-1):
  X1,Y1 = fish[i][0]-1,fish[i][1]-1
  for j in range(i+1,M):
    X2,Y2 = fish[j][0]-1,fish[j][1]-1
    X,Y = abs(X2-X1),abs(Y2-Y1)
    if X + Y <= L:
      Lx = min(X1,X2)
      Rx = max(X1,X2)
      Ly = min(Y1,Y2)
      Ry = max(Y1,Y2)
      for k in range(max(1,X),L-Y+1):
        find(Lx,Ly,Lx+k,Ly+L-k)
        find(Rx-k,Ry-L+k,Rx,Ry)

if 2*L > 4*N:
  print(0)
else:
  print(ans)
