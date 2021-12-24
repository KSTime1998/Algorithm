# 1670 - 정상 회담 2 (Gold 3)
import sys
N = int(sys.stdin.readline())
dp = [0]*(N//2+1)
dp[0] = 1
for n in range(1,N//2+1):
  a = 0
  while a < n:
    dp[n] += (dp[a] * dp[n-a-1])%987654321
    a += 1
  dp[n] %= 987654321
print(dp[-1])
