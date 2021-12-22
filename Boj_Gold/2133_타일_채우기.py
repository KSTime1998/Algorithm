# 2133 - 타일 채우기 (Gold 5)
import sys
N = int(sys.stdin.readline())
space = [[0,0,0] for _ in range(N+1)]
space[1][1] = 1
space[0][2] = 1
for i in range(2,N+1):
  if i%2 == 0:
    space[i][0] = space[i-1][1]
    space[i][2] = space[i][0]*2 + space[i-2][2]
  else:
    space[i][1] = space[i-1][0] + space[i-1][2]
print(space[-1][-1])
