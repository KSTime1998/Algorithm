# 10986 - 나머지 합 (TLE)
import sys
N,M = map(int,sys.stdin.readline().split())
number = list(map(int,sys.stdin.readline().split()))
ans = 0
checked = set()

for left in range(N):
  if left in checked:
    continue
  a = cnt = 0
  for right in range(left,N):
    a += number[right]
    if a%M == 0:
      checked.add(left)
      left = right + 1
      cnt += 1
      ans += cnt
      continue
  checked.add(left)

print(ans)
