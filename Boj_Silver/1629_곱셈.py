# 1629 - 곱셈 (Silver 1)
import sys
A,B,C = map(int,sys.stdin.readline().split())

def multiply(a,b):
  if b == 1:
    return a%C
  
  else:
    B_2 = multiply(a,b//2)
    if b//2 == 0:
      return B_2 * B_2 % C
    else:
      return B_2 * B_2 * A % C

print(multiply(A,B))
