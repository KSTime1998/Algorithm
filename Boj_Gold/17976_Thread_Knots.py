# 17976 - Thread Knots (Gold 3) - ?
# 가장 가까운 두 매듭 사이의 거리가 최대 몇까지 될 수 있는가?
import sys
n = int(sys.stdin.readline())
thread = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(n)], key = lambda x : x[0])

def calculate(distance):
  location = thread[0][0]
  for i in range(1,n):
    if location + distance < thread[i][0]:
      location = thread[i][0]
    elif location + distance <= sum(thread[i]):
      location += distance
    else:
      return True
  return False

left = 0
right = 2*10**9+1
while right > left:
  mid = (left + right)//2
  if calculate(mid):
    right = mid
  else:
    left = mid + 1

print(left-1)
