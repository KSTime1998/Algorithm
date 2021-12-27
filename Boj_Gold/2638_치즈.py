# 2638 - 치즈 (Gold 4)
import sys
N,M = map(int,sys.stdin.readline().split())
space = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
T = 0
D = [[0,1],[0,-1],[1,0],[-1,0]]

def air(x,y):
  for i,j in D:
    X = x+i
    Y = y+j
    if 0<=X<N and 0<=Y<M and space[X][Y] == 0:
      space[X][Y] = -1
      air(X,Y)

space[0][0] = -1
air(0,0)
cheese = 0
for i in range(N):
  for j in range(M):
    if space[i][j] == 1:
      cheese += 1

while cheese > 0:
  T += 1
  for i in range(N):
    for j in range(M):
      if space[i][j] == 1:
        cnt = 0
        for x,y in D:
          X = i+x
          Y = j+y
          if space[X][Y] == -1:
            cnt += 1
          if cnt > 1:
            break
        if cnt > 1:
          space[i][j] = 0
          cheese -= 1

  for i in range(N):
    for j in range(M):
      if space[i][j] == 0:
        for x,y in D:
          X = i+x
          Y = j+y
          if space[X][Y] == -1:
            space[i][j] = -1
            air(i,j)

print(T)
