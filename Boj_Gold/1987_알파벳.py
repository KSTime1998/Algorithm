# 1987 - 알파벳 (Gold 4)
import sys
R,C = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
ans = 0
used_alphabet = set()

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def dfs(x,y,val):
  global ans
  ans = max(ans, val)
  for d in range(4):
    X,Y = x+dx[d],y+dy[d]
    if 0 <= X < R and 0 <= Y < C:
      if board[X][Y] in used_alphabet:
        continue
      used_alphabet.add(board[X][Y])
      dfs(x+dx[d],y+dy[d],val+1)
      used_alphabet.remove(board[X][Y])

used_alphabet.add(board[0][0])
dfs(0,0,1)
print(ans)
