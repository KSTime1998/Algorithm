# 9663 - N-Queen (Gold 5)
import sys
N = int(sys.stdin.readline())

def chess(n,visit):
  global cnt
  can = [1] * N
  for i in range(len(visit)):
    v = visit[i]
    can[v] = 0
    for j in range(-1,2,2):
      if 0 <= v + (j*(n-i)) <= N-1:
        can[v + (j*(n-i))] = 0

  if n == N-1:
    cnt += can.count(1)
  else:
    for a in range(N):
      if can[a] != 0:
        chess(n+1,visit+[a])

if N == 1:
  print(1)
elif 1 < N < 4:
  print(0)
else:
  cnt = 0
  for i in range(N):
    chess(1,[i])
  print(cnt)
