# 17144 - 미세먼지 안녕! (Gold 4)
import sys
R,C,T = map(int,sys.stdin.readline().split())
area = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]
D = [[0,1],[0,-1],[1,0],[-1,0]]

for i in range(R):
  if area[i][0] == -1:
    A = i
    break

def Diffusion():
  diffusion = [[0] * (C) for _ in range(R)]
  for i in range(R):
    for j in range(C):
      dust = area[i][j]
      if dust >= 5:
        for x,y in D:
          X = i+x
          Y = j+y
          if 0 <= X < R and 0 <= Y < C and area[X][Y] != -1:
            diffusion[X][Y] += dust//5
            area[i][j] -= dust//5
  for i in range(R):
    for j in range(C):
      area[i][j] += diffusion[i][j]

def Moving():
  for up1 in range(A-1,0,-1):
    area[up1][0] = area[up1-1][0]
  for down1 in range(A+2,R-1):
    area[down1][0] = area[down1+1][0]

  for cycle2 in range(0,C-1):
    area[0][cycle2] = area[0][cycle2+1]
    area[-1][cycle2] = area[-1][cycle2+1]

  for up2 in range(0,A):
    area[up2][-1] = area[up2+1][-1]
  for down2 in range(R-1,A+1,-1):
    area[down2][-1] = area[down2-1][-1]

  for cycle4 in range(C-1,1,-1):
    area[A][cycle4] = area[A][cycle4-1]
    area[A+1][cycle4] = area[A+1][cycle4-1]
  area[A][1] = area[A+1][1] = 0

while T > 0:
  T -= 1
  Diffusion()
  Moving()

ans = 0
for i in range(R):
  for j in range(C):
    ans += area[i][j]
print(ans+2)
