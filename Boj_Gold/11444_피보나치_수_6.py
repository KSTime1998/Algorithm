# 11444 - 피보나치 수 6 (Gold 2)
import sys
def multiply(m1,m2):
  M = [[0,0],[0,0]]
  for i in range(2):
    for j in range(2):
      a = 0
      for k in range(2):
        a = (a + m1[i][k]*m2[k][j])%1000000007
      M[i][j] = a
  return M

fibo_matrix = [[1,1],[1,0]]
n = int(sys.stdin.readline()) - 1
b = []
while n > 0:
  cnt = 0
  while 2**cnt <= n:
    cnt += 1
  cnt -= 1
  n -= 2**cnt
  m = fibo_matrix[:]
  for _ in range(cnt):
    m = multiply(m,m)
  b.append(m)

ans = b[0]
for n in range(1,len(b)):
  ans = multiply(ans,b[n])

print(ans[0][0])
