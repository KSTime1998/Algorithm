# 6209 - 제자리 멀리뛰기 (Gold 2)
import sys
D,N,M = map(int,sys.stdin.readline().split())
stone = sorted([int(sys.stdin.readline()) for _ in range(N)])

def possible(d):
  removed = set()
  now = 0

  for i in range(N):
    next = stone[i]
    if next - now >= d:
      now = next
    else:
      removed.add(i)
    if len(removed) > M:
      return False

  i = N-1
  while D - stone[i] < d:
    removed.add(i)
    i -= 1
    if len(removed) > M or i < 0:
      return False

  return True

if N == 0:
  print(D)

else:
  right = D
  left = 0
  while right > left:
    mid = (right + left)//2
    if possible(mid):
      left = mid + 1
    else:
      right = mid

  print(left-1)
