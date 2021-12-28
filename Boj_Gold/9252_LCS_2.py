# 9252 - LCS 2 (Gold 5) - 죽여버리고싶다 진짜
import sys
sys.setrecursionlimit(10**5)
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

l1 = len(s1)
l2 = len(s2)
dp = [[0]*(l1+1) for _ in range(l2+1)]

for i in range(1,l2+1):
  for j in range(1,l1+1):
    if s1[j-1] == s2[i-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])
if dp[-1][-1] != 0:
  ans = []
  start = dp[-1][-1]
  I = l2
  J = l1
  while start > 0:
    if dp[I][J-1] == dp[I-1][J] == start-1:
      ans.append(s1[J-1])
      start -= 1
      I -= 1
      J -= 1
    else:
      if dp[I-1][J] == start:
        I -= 1
      else:
        J -= 1
  print(''.join(map(str,ans[::-1])))
