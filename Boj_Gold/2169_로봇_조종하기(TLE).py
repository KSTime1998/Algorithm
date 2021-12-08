# 2169 - 로봇 조종하기 (Gold 1) - 시간초과
import sys
N,M = map(int,sys.stdin.readline().split())
region = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ANS = 0
SUM = [[[[] for _ in range(M)] for _ in range(M)] for _ in range(N)]

# 시작지점이 s로 주어진다.
def maxvalue(n,s,startval):
  global ANS

  # 가장 아래층이라면 우측을 전부 더해줘야만 한다.
  if n == M-1:
    ANS = max(sum(region[n][s:])+startval,ANS)

  else:
    # 왼쪽 무빙
    for m in range(0,s):
      sum(region[n][m:s+1])
      maxvalue(n+1,m,startval+SUM[n][m][s]))
    # 오른쪽 무빙
    for m in range(s,M):
      sum(region[n][m:s+1])
      maxvalue(n+1,m,startval+SUM[n][m][s]))

maxvalue(0,0,0)
print(ANS)
