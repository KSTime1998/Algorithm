# 1630 - 오민식 (Gold 4)
import sys
N = int(sys.stdin.readline())
prime = [0]*(N+1)
ans = 1

for i in range(2,N+1):
  if prime[i] == 0:
    a = 2*i
    while a <= N:
      prime[a] = 1
      a += i
    a = i
    while a <= N:
      a *= i
    ans = (ans*(a//i))%987654321
print(ans)
