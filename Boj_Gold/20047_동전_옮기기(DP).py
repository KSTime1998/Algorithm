# 20047 - 동전 옮기기 (Gold 2) - DP
import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
i,j = map(int,sys.stdin.readline().split())

coin = [S[i],S[j]]
S_removed = S[:i] + S[i+1 : j] + S[j+1:]

s1 = [1]*(N-1)
for a in range(0,N-2):
  if S_removed[a] != T[a] or s1[a] == 0:
    s1[a+1] = 0

s2 = [0]*(N-1)
s3 = [0]*(N)
for a in range(0,N-1):
  if (s1[a] == 1 and T[a] == coin[0]) or (s2[a-1] == 1 and T[a] == S_removed[a-1]):
    s2[a] = 1

for a in range(1,N):
  if (s1[a-1] == 1 and T[a-1] == coin[0] and T[a] == coin[1]) or (s2[a-1] == 1 and T[a] == coin[1]) or (s3[a-1] == 1 and T[a] == S_removed[a-2]):
    s3[a] = 1

if s3[-1] == 1:
  print('YES')
else:
  print('NO')
