# 1006 - 습격자 초라기 (Platinum 3) - 시간초과...
import sys
sys.setrecursionlimit(10**6)

def same_comparison(u,d,cnt,U,D):
  if same[u] > cnt:
      same[u] = cnt
      attack(u,d,cnt,U,D)

def upper_comparison(u,d,cnt,U,D):
  if upper[u] > cnt:
    upper[u] = cnt
    attack(u,d,cnt,U,D)

def lower_comparison(u,d,cnt,U,D):
  if lower[d] > cnt:
    lower[d] = cnt
    attack(u,d,cnt,U,D)


def attack(u,d,cnt,U,D):
  global ANS
  if (U-u + D-d)//2 + cnt > ANS:
    return

  if u >= N-1 or d >= N-1:
    if u == N:
      if d != N and D != 1:
        cnt +=1
    
    elif d == N:
      if u != N and U != 1:
        cnt += 1

    elif u == N-1 and d == N-1:
      if U == 1 or D == 1 or s1[u] + s2[d] <=W:
        cnt += 1
      else:
        cnt += 2

    elif u == N-1 and d == N-2:
      if s2[d] + s2[d+1] <= W:
        if U == 1:
          cnt += 1
        else:
          cnt += 2
      elif s1[u] + s2[d+1] <= W or U == 1:
        cnt += 2
      else:
        cnt += 3

    elif d == N-1 and u == N-2:
      if s1[u] + s1[u+1] <= W:
        if D == 1:
          cnt += 1
        else:
          cnt += 2
      elif s2[d] + s1[u+1] <= W or D == 1:
        cnt += 2
      else:
        cnt += 3
    ANS = min(ANS,cnt)

  else:
    if u == d:
      if s1[u] + s2[d] <= W:
        same_comparison(u+1,d+1,cnt+1,U,D)
      if s1[u] + s1[u+1] <= W:
        if s2[d] + s2[d+1] <= W:
          same_comparison(u+2,d+2,cnt+2,U,D)
        upper_comparison(u+2,d+1,cnt+2,U,D)
      if s2[d] + s2[d+1] <= W:
        lower_comparison(u+1,d+2,cnt+2,U,D)
      same_comparison(u+1,d+1,cnt+2,U,D)
    
    elif u > d:
      if s2[d] + s2[d+1] <= W:
        lower_comparison(u,d+2,cnt+1,U,D)
      same_comparison(u,d+1,cnt+1,U,D)
    
    elif u < d:
      if s1[u] + s1[u+1] <= W:
        upper_comparison(u+2,d,cnt+1,U,D)
      same_comparison(u+1,d,cnt+1,U,D)

for _ in range(int(sys.stdin.readline())):
  N,W = map(int,sys.stdin.readline().split())
  s1 = list(map(int,sys.stdin.readline().split()))
  s2 = list(map(int,sys.stdin.readline().split()))
  ANS = 2*N
  same = [2*N] * (N+1)
  upper = [2*N] * (N+1)
  lower = [2*N] * (N+1)
  if s1[-1] + s1[0] <= W:
    if s2[-1] + s2[0] <= W:
      attack(1,1,2,1,1)
    attack(1,0,1,1,0)
  if s2[-1] + s2[0] <= W:
    attack(0,1,1,0,1)
  attack(0,0,0,0,0)

  print(ANS)
