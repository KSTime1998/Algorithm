# 13172 - 시그마 (Gold 5)
import sys
from math import gcd
X = 1000000007

def modular(a,b):
  return (a * b_X(b,X-2))%X

def b_X(val,exp):
  if exp == 1:
    return val

  if exp % 2 == 0:
    h = b_X(val,exp//2)
    return (h*h)%X

  else:
    return (val * b_X(val,exp-1))%X

M = int(sys.stdin.readline())
ans = 0
for _ in range(M):
  n, s = map(int, input().split())
  g = gcd(n,s)
  n //= g
  s //= g

  ans += modular(s,n)
  ans %= X

print(ans)
