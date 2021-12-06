# 12015 - 가장 긴 증가하는 부분 수열 2 (Gold 2)
N = int(input())
A = list(map(int,input().split()))

def id(x):
  if lis[-1] < x:
    lis.append(x)
    return
  mx = len(lis)
  mn = 0
  while mn < mx:
    a = (mx+mn)//2
    if lis[a] >= x:
      mx = a
    else:
      mn = a+1
  lis[mx] = x

lis = [0]
for i in A:
  id(i)

print(len(lis)-1)
