# 1987 - 알파벳 (Gold 4)
import sys
R,C = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
ans = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
  global ans
  alpha = set()
  alpha.add((0,0,board[0][0]))

  while alpha:
    x,y,al = alpha.pop()
    ans = max(ans, len(al))
    for d in range(4):
      X,Y = x+dx[d],y+dy[d]
      if 0 <= X < R and 0 <= Y < C:
        if board[X][Y] in al:
          continue
        alpha.add((X,Y,al+board[X][Y]))

bfs()
print(ans)
