# 2467 - 용액 (Gold 5) - 스스로 못품
import sys
N = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))
minval = 2000000001
left = 0
right = N-1
while left < right:
  val = number[left] + number[right]
  if abs(val) < minval:
    minval = abs(val)
    ans = [number[left],number[right]]

  if val > 0:
    right -= 1
  elif val < 0:
    left += 1
  else:
    break

print(' '.join(map(str,ans)))
