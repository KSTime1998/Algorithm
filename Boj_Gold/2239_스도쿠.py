# 2239 - 스도쿠 (Gold 4)
import sys
arr = [list(sys.stdin.readline().rstrip()) for _ in range(9)]
fixed = [[False for _ in range(9)] for _ in range(9)]
Possible = False

for i in range(9):
  for j in range(9):
    arr[i][j] = int(arr[i][j])
    if arr[i][j] != 0:
      fixed[i][j] = True

def dfs(P):
  global Possible
  if P == 81:
    Possible = True
    for a in arr:
      print(''.join(map(str,a)))
    return

  x,y = P//9,P%9
  if fixed[x][y]:
    dfs(P+1)

  else:
    for v in range(1,10):
      print(P,v)
      V = True
      for i in range(9):
        if arr[i][y] == v or arr[x][i] == v:
          V = False
          break

      if V:
        x3,y3 = x//3,y//3
        for X in range(x3*3,x3*3+3):
          for Y in range(y3*3,y3*3+3):
            if arr[X][Y] == v:
              V = False
              break

        if V:
          arr[x][y] = v
          dfs(P+1)

          if Possible:
            return

          arr[x][y] = 0

dfs(0)
