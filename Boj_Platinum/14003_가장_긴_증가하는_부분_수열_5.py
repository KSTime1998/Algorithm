# 14003 - 가장 긴 증가하는 부분 수열 5 (Platinum 5)
import sys
def binary(L,I):
  left = 0
  right = len(L) - 1
  while right > left:
    mid = (right + left)//2
    if L[mid] >= I:
      right = mid
    else:
      left = mid+1
  return left

N = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))

lis = [number[0]]
lis_ind = [[0]]
for i in range(1,N):
  n = number[i]
  if n > lis[-1]: 
    lis.append(n)
    lis_ind.append([i])
  else:
    a = binary(lis,n)
    lis[a] = n
    lis_ind[a].append(i)

ind = lis_ind[-1][0]
lis[-1] = number[ind]
for i in range(len(lis)-2,-1,-1):
  I = lis_ind[i]
  if I[-1] < ind:
    ind = I[-1]
    lis[i] = number[ind]
  else:
    a = binary(I,ind)
    ind = I[a-1]
    lis[i] = number[ind]

print(len(lis))
print(' '.join(map(str,lis)))
