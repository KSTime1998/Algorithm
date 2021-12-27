# 2166 - 다각형의 면적 (Gold 5)
import sys
import math
N = int(sys.stdin.readline())
figure = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
X = Y = 0
for i in range(0,N):
    X += figure[i][0] * figure[i-1][1]
    Y += figure[i][1] * figure[i-1][0]

print(round((X - Y)/2,1))
