# 10026 - 적록색약 (Gold 5)
import sys
N = int(sys.stdin.readline())
space = [sys.stdin.readline().rstrip() for _ in range(N)]

visit = [[[0,0] for _ in range(N)] for _ in range(N)]
D = [[1,0],[-1,0],[0,1],[0,-1]]
answer = [0,0]

def sector(start,color,dichromacy):
  left = 0
  right = 1
  while right > left:
    for k in range(left,len(start)):
      for d in D:
        x = start[k][0] + d[0]
        y = start[k][1] + d[1]
        if 0 <= x < N and 0 <= y < N and space[x][y] == color and visit[x][y][dichromacy] == 0:
          visit[x][y][dichromacy] = 1
          start.append([x,y])
        elif  0 <= x < N and 0 <= y < N and color != 'B' and space[x][y] != 'B' and dichromacy == 1 and visit[x][y][dichromacy] == 0:
          visit[x][y][1] = 1
          start.append([x,y])
    left = right
    right = len(start)

for i in range(N):
  for j in range(N):
    if visit[i][j][0] == 0:
      answer[0] += 1
      visit[i][j][0] = 1
      sector([[i,j]],space[i][j],0)
    if visit[i][j][1] == 0:
      answer[1] += 1
      visit[i][j][1] = 1
      sector([[i,j]],space[i][j],1)

print(' '.join(str(x) for x in answer))
