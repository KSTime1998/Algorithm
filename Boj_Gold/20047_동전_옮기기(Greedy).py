# 20047 - 동전 옮기기 (Gold 2) - 그리디
import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
i,j = map(int,sys.stdin.readline().split())

coin = [S[i],S[j]]
S_removed = S[:i] + S[i+1 : j] + S[j+1:]

Fail = Possible = 0
for left in range(0,N-2):
  if S_removed[left] != T[left]:
    if coin[0] == T[left]:

      for mid in range(left,N-2):
        if S_removed[mid] != T[mid+1]:
          if coin[1] == T[mid+1]:

            for right in range(mid,N-2):
              if S_removed[right] != T[right+2]:
                Fail = 1
                break
            if Fail == 0:
              Possible = 1
            break
        
          else:
            Fail = 1
            break

      if (Fail == 0 and coin[1] == T[-1]) or Possible == 1:
        Possible = 1
      else:
        Fail = 1
      break

    else:
      Fail = 1
      if coin[1] != T[left]:
        Possible = -1
      break
if Possible == 1 or (Fail == 0 and coin[0] == T[-2] and coin[1] == T[-1]):
  print('YES')
else:
  Fail = Possible = 0
  for right in range(N-3,-1,-1):
    if S_removed[right] != T[right+2]:
      if coin[1] == T[right+2]:

        for mid in range(right,-1,-1):
          if S_removed[mid] != T[mid+1]:
            if coin[0] == T[mid+1]:

              for left in range(mid,-1,-1):
                if S_removed[left] != T[left]:
                  Fail = 1
                  break
              if Fail == 0:
                Possible = 1

            else:
              Fail = 1
              break

        if (Fail == 0 and coin[0] == T[0]) or Possible == 1:
          Possible = 1
        else:
          Fail = 1
        break

      else:
        Fail = 1
        break

  if Possible == 1 or (Fail == 0 and coin[0] == T[0] and coin[1] == T[1]):
    print('YES')
  else:
    print('NO')
