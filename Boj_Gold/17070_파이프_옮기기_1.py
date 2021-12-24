# 17070 - 파이프 옮기기 1 (Gold 5)
import sys
N = int(sys.stdin.readline())
space = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
counting = [[[0,0,0] for _ in range(N+1)] for _ in range(N+1)]
counting[1][2][0] = 1

for i in range(1,N+1):
  for j in range(2,N+1):
    if space[i-1][j-1] == 0:
      counting[i][j][0] += counting[i][j-1][0] + counting[i][j-1][2]
      counting[i][j][1] += counting[i-1][j][1] + counting[i-1][j][2]
      if space[i-2][j-1] == 0 and space[i-1][j-2] == 0:
        counting[i][j][2] += counting[i-1][j-1][2] + counting[i-1][j-1][1] + counting[i-1][j-1][0]

print(sum(counting[-1][-1]))
