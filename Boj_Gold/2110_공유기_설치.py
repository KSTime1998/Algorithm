# 2110 - 공유기 설치 (Gold 5)
import sys
N,C = map(int,sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline()) for _ in range(N)])

def connect(x):
  location = house[0]
  n = 1
  for i in range(1,N):
    h = house[i]
    if h - location >= x:
      location = h
      n += 1
    if n >= C:
      return True
  if n < C:
    return False

minlength = 0
maxlength = 1000000000
while maxlength > minlength:
  mid = (minlength + maxlength)//2
  if connect(mid):
    minlength = mid + 1
  else:
    maxlength = mid

print(maxlength-1)
