# 2206 - 벽 부수고 이동하기 (Gold 4)
import sys
N,M = map(int,sys.stdin.readline().split())
Map = []
for _ in range(N):
  m = []
  for i in sys.stdin.readline().rstrip():
    m.append(int(i))
  Map.append(m)

start = [[0]*M for _ in range(N)]
end = [[0]*M for _ in range(N)]
D = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(s,length):
  v = [s]
  left = 0
  right = l = 1
  while right > left:
    l += 1
    for V in range(left,right):
      x = v[V][0]
      y = v[V][1]
      for i,j in D:
        X = x+i
        Y = y+j
        if 0 <= X < N and 0 <= Y < M and Map[X][Y] == 0 and length[X][Y] == 0:
          length[X][Y] = l
          v.append([X,Y])
    left = right
    right = len(v)

start[0][0] = end[-1][-1] = 1
bfs([0,0],start)
bfs([N-1,M-1],end)

if start[-1][-1] == 0:
  minlength = 1000000000
else:
  minlength = start[-1][-1]

for i in range(N):
  for j in range(M):
    if Map[i][j] == 1:
      for x in range(4):
        for y in range(4):
          x1,y1 = i+D[x][0],j+D[x][1]
          x2,y2 = i+D[y][0],j+D[y][1]
          if x1 != x2 or y1 != y2:
            if 0<=x1<N and 0<=y1<M and 0<=x2<N and 0<=y2<M and start[x1][y1]*end[x2][y2] != 0:
              minlength = min(minlength,start[x1][y1]+end[x2][y2]+1)

if minlength == 1000000000:
  print(-1)
else:
  print(minlength)
