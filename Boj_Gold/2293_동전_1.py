# 2293 - 동전 1 (Gold 5)
import sys
N,K = map(int,sys.stdin.readline().split())
coin = sorted([int(sys.stdin.readline()) for _ in range(N)],reverse=True)
number = [0]*(K+1)
number[0] = 1

for i in coin:
  for j in range(i,K+1):
    if j-i >= 0:
      number[j] += number[j-i]

print(number[-1])
