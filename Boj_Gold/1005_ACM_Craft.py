# 1005 - ACM Craft (Gold 3)
import sys
T = int(sys.stdin.readline())

def t(x):
  if Et[x] == -1:
    if btr[x] == []:
      Et[x] = bti[x]
    else:
      val = 0
      for i in btr[x]:
        if t(i) >= val:
          val = t(i)
      Et[x] = val + bti[x]
    return Et[x]
  else:
    return Et[x]

for i in range(T):
  N, K = map(int, sys.stdin.readline().split())
  bti = list(map(int, sys.stdin.readline().split()))
  bti.insert(0,0)
  btr = [[] for i in range(N+1)]
  Et = [-1 for i in range(N+1)]

  for j in range(K):
    req, num = map(int, sys.stdin.readline().split())
    btr[num].append(req)

  print(t(int(sys.stdin.readline())))
