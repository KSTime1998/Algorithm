# 9251 - LCS (Gold 5)
import sys
str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
str2set = set(str2)
LCS = []

for i in range(len(str1)):
  if str1[i] in str2set:
    LCS = [str2.find(str1[i])]
    start = i
    break

for i in range(i+1,len(str1)):
  s = str1[i]
  if s not in str2set:
    continue
  for j in range(len(LCS)-1,-1,-1): 
    if j == len(LCS)-1:
      a = str2[LCS[-1]+1:].find(s)
      if a != -1:
        LCS.append(a + 1 + LCS[-1])
    if j == 0:
      LCS[0] = min(str2.find(s),LCS[0])
    elif j > 0:
      b = str2[LCS[j-1]+1:].find(s)
      if b != -1:
        LCS[j] = min(b + LCS[j-1] + 1, LCS[j])

print(len(LCS))
