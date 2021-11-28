# 1011 - Fly me to the Alpha Centauri (Gold 5)
import math
T = int(input())

for i in range(T):
  x,y = map(int,input().split())
  r = y-x
  cnt = 0
  n = math.floor(r**(1/2))
  cnt += 2*n - 1
  r -= n**2
  while True:
    cnt += r//n
    r = r%n
    if r == 0 :
      print(cnt)
      break
    else:
      n -= 1
