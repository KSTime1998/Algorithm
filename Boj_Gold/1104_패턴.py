# 1104 - 패턴 (Gold 1)
import sys
S1 = sys.stdin.readline().rstrip()
S2 = sys.stdin.readline().rstrip()
C = int(sys.stdin.readline())

def is_in_S(s1,s2):
  cnt = 0
  S = s1+s2
  for i in range(len(S)):
    s = S[i]
    if s == '0':
      if cnt == 0:
        first_s = i
      cnt += 1
      if C == cnt:
        return first_s
    else:
      cnt = 0
  return -1

ans = is_in_S(S1,S1)
if ans != -1:
  print(ans)

else:
  if '1' not in S1:
    if '1' not in S2:
      print(0)
    else:
      left_S2 = right_S2 = 0
      for i in S2:
        if i == '0':
          right_S2 += 1
        else:
          break
      for i in range(len(S2)):
        if S2[i] == '0':
          if left_S2 == 0:
            loc = i
          left_S2 += 1
        else:
          left_S2 = 0
      if len(S1)*1000000 + right_S2 >= C:
        print(0)
      elif left_S2 + right_S2 + len(S1)*1000000 >= C:
        print(len(S1)*1000000 + loc)
      else:
        print(-1)

  else:
    ans = is_in_S(S1+S2,S1)
    if ans != -1:
      print(ans+999999*len(S1))
    
    else:
      ans = is_in_S(S1+S2,S2+S1)
      if ans != -1:
        print(ans+1999999*len(S1) + len(S2))
            
      else:
        if '1' in S2:
          print(-1)
        
        else:
          left_S1 = 0
          right_S1 = 0
          for i in S1:
            if i == '0':
              right_S1 += 1
            else:
              break
          for i in S1:
            if i == '0':
              left_S1 += 1
            else:
              left_S1 = 0

          l1 = 1000000*len(S1)
          l2 = len(S2)
          n = (C - right_S1 - left_S1)//l2 + 1
          while right_S1 + left_S1 + (n-1)*l2 >= C:
            n -= 1

          ans = l1*n + (n*(n-1)*l2)//2 - left_S1
          if ans + C >= 10000000000000000-1:
            print(-1)
          else:
            print(ans)
