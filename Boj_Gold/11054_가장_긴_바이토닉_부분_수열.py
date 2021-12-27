# 11054 - 가장 긴 바이토닉 부분 수열 (Gold 3)
import sys
N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
LIS = [1]
LDS = [1]*N
for i in range(1,N):
  lis = 1
  for j in range(i):
    if num[j] < num[i]:
      lis = max(LIS[j]+1,lis)
  LIS.append(lis)
for i in range(N-2,-1,-1):
  lds = 1
  for j in range(N-1,i,-1):
    if num[j] < num[i]:
      lds = max(LDS[j]+1,lds)
  LDS[i] = lds

length = 0
for i in range(N):
  length = max(LIS[i]+LDS[i],length)
print(length-1)
