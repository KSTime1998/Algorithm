# 10986 - 나머지 합 (Gold 3) - 스스로 못 풀었다 / 미제출
import sys
N,M = map(int,sys.stdin.readline().split())
number = list(map(int,sys.stdin.readline().split()))
remain = [0]*(M)
value = 0
for n in range(N):
  value = (value + number[n])%M
  remain[value] += 1

ans = 0
for m in range(M):
  if m == 0:
    ans += remain[m] * (remain[m] + 1) // 2
  else:
    ans += remain[m] * (remain[m] - 1) // 2
print(ans)
