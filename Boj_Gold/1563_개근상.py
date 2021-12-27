# 1563 - 개근상 (Gold 4)
import sys
N = int(sys.stdin.readline())
dp = [[1,0,0]] + [[0,0,0] for _ in range(N)]
for i in range(1,N+1):
  dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
  dp[i][1] = dp[i-1][0]
  dp[i][2] = dp[i-1][1]

# i번째에 L을 넣는 경우 = 1~i-1번째까지 O,A로만 만드는 경우 * i+1~N번째까지 O,A로만 만드는 경우
# L을 안 쓰는 경우 = 1~N번쨰까지 O,A로만 만드는 경우
ans = (sum(dp[N]))%1000000
for i in range(1,N+1):
  ans = (ans + sum(dp[i-1]) * sum(dp[N-i]))%1000000

print(ans)
