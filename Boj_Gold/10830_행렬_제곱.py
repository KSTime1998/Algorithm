# 10830 - 행렬 제곱 (Gold 4)
import sys
N,B = map(int,sys.stdin.readline().split())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
  for j in range(N):
    matrix[i][j] %= 1000

def multiply(M1,M2):
  M = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      a = 0
      for k in range(N):
        a = (a + M1[i][k]*M2[k][j])%1000
      M[i][j] = a
  return M

b = []
while B > 0:
  cnt = 0
  while 2**cnt <= B:
    cnt += 1
  cnt -= 1
  B -= 2**cnt
  m = matrix[:]
  for _ in range(cnt):
    m = multiply(m,m)
  b.append(m)

ans = b[0]
for n in range(1,len(b)):
  ans = multiply(ans,b[n])

for i in ans:
  print(' '.join(map(str,i)))
