# 1937 - 욕심쟁이 판다 (Gold 3)
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
bamboo = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
days = [[1]*n for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(i,j):
  for d in range(4):
    X = i + dx[d]
    Y = j + dy[d]
    if 0 <= X < n and 0 <= Y < n:
      if bamboo[X][Y] < bamboo[i][j]:
        if days[X][Y] != 1:
          days[i][j] = max(days[X][Y]+1,days[i][j])          
        if days[X][Y] == 1:
          dfs(X,Y)
          days[i][j] = max(days[X][Y]+1,days[i][j])

ans = 0
for x in range(n):
  for y in range(n):
    if days[x][y] == 1:
      dfs(x,y)
    ans = max(ans,days[x][y])
print(ans)
