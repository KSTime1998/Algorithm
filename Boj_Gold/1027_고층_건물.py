# 1027 - 고층 건물 (Gold 4)
import sys
N = int(sys.stdin.readline())
buildings = list(map(int,sys.stdin.readline().split()))
ans = 0

def cansee(now,see,distance):
  global cnt, heightlimit
  if (buildings[see] - buildings[now])/distance > heightlimit:
    cnt += 1
    heightlimit = (buildings[see] - buildings[now])/distance

for i in range(N):
  cnt = 0
  heightlimit = -1000000001
  for left in range(i-1,-1,-1):
    cansee(i,left,i-left)
  heightlimit = -1000000001
  for right in range(i+1,N):
    cansee(i,right,right-i)
  ans = max(ans,cnt)

print(ans)
