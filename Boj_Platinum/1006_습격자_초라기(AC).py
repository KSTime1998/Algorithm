# 1006 - 습격자 초라기 (Platinum 3)
import sys

def attack(U,D):
  global ans
  same = [0] * N
  upper = [0] * N
  lower= [0] * N
  lower[0] = upper[0] = 1
  lower[1] = upper[1] = 3
  same[0] = 2
  same[1] = 3

  if U == 1 and D == 0:
    if s2[0] + s2[1] <= W:
      lower[1] = 2
    elif s1[1] + s2[1] > W:
      same[1] = 4

  elif D == 1 and U == 0:
    if s1[0] + s1[1] <= W:
      upper[1] = 2
    elif s1[1] + s2[1] > W:
      same[1] = 4

  elif D == U == 0:
    if s1[0] + s2[0] <= W:
      same[0] = 1
      upper[1] = lower[1] = 2
      if s1[1] + s2[1] <= W:
        same[1] = 2
    if s1[0] + s1[1] <= W:
      upper[1] = 2
      if s2[0] + s2[1] <= W:
        lower[1] = 2
        same[1] = 2
    elif s2[0] + s2[1] <= W:
      lower[1] = 2
    elif s1[0] + s2[0] > W and s1[1] + s2[1] > W:
      same[1] = 4

  elif s1[1] + s2[1] > W:
    same[1] = 4

  for n in range(2,N):
    s = set()
    u = {same[n-1]+1}
    d = {same[n-1]+1}
    if s1[n] + s2[n] <= W:
      s.add(same[n-1] + 1)
      s.add(upper[n-1] + 2)
      s.add(lower[n-1] + 2)
    else:
      s.add(same[n-1] + 2)

    if s1[n-1] + s1[n] <= W:
      s.add(same[n-2] + 3)
      s.add(lower[n-1] + 2)
      u.add(lower[n-1] + 1)
      u.add(same[n-2] + 2)
      if s2[n-1] + s2[n] <= W:
        s.add(same[n-2] + 2)

    if s2[n-1] + s2[n] <= W:
      s.add(same[n-2] + 3)
      s.add(upper[n-1] + 2)
      d.add(same[n-2] + 2)
      d.add(upper[n-1] + 1)

    same[n] = min(s)
    upper[n] = min(u)
    lower[n] = min(d)

  if U == 1:
    if D == 1:
      ans = min(ans,same[-2])
    else:
      ans = min(ans,lower[-1])
  elif D == 1:
    ans = min(ans,upper[-1])
  else:
    ans = min(ans,same[-1])

for i in range(int(sys.stdin.readline())):
  N,W = map(int,sys.stdin.readline().split())
  s1 = list(map(int,sys.stdin.readline().split()))
  s2 = list(map(int,sys.stdin.readline().split()))
  if N == 1:
    if s1[0] + s2[0] <= W:
      print(1)
    else:
      print(2)
  else:
    ans = 2*N + 1
    attack(0,0)
    if s1[-1] + s1[0] <= W:
      attack(1,0)
      if s2[-1] + s2[0] <= W:
        attack(1,1)
    if s2[-1] + s2[0] <= W:
      attack(0,1)

    print(ans)
