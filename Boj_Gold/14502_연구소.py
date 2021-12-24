# 14502 - 연구소 (Gold 5)
import sys
N,M = map(int,sys.stdin.readline().split())
space = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = 0
safe = -3
start = set()
for x in range(N):
  for y in range(M):
    if space[x][y] == 2:
      start.add((x,y))
    if space[x][y] == 0:
      safe += 1
D = [[1,0],[0,1],[-1,0],[0,-1]]

def virus(x,y):
  global cnt
  if safe-cnt <= ans:
    return 
  for i,j in D:
    X=x+i
    Y=y+j
    if 0<=X<N and 0<=Y<M and space[X][Y] == 0:
      cnt += 1
      space[X][Y] = -1
      virus(X,Y)

def clearing():
  for x in range(N):
    for y in range(M):
      if space[x][y] == -1:
        space[x][y] = 0

for x1 in range(N):
  for y1 in range(M):
    if space[x1][y1] != 0:
      continue
    for x2 in range(N):
      for y2 in range(M):
        if space[x2][y2] != 0 or (x1==x2 and y1==y2):
          continue
        for x3 in range(N):
          for y3 in range(M):
            if (x1==x3 and y1==y3) or (x2==x3 and y2==y3) or space[x3][y3] != 0:
              continue
            else:
              space[x1][y1] = space[x2][y2] = space[x3][y3] = 1
              cnt = 0
              for x,y in start:
                virus(x,y)
              ans = max(ans,safe-cnt)
              clearing()
              space[x1][y1] = space[x2][y2] = space[x3][y3] = 0

print(ans)
