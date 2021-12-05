# 9251 - LCS (Gold 5) - 힘든 싸움이었다
#str1,str2 = input().split()
str2set = set(str2)
LCS = []
for s in str1:
  if s in str2set:
    LCS = [str2.find(s)]
    break

for i in range(0,len(str1)):
  s = str1[i]
  if s not in str2set:
    continue
  for J in range(1,len(LCS)+1):
    j = -J
    if j == -len(LCS):
      LCS[0] = min(str2.find(s),LCS[0])
    if j == -1 and str2[LCS[-1]+1:].find(s) != -1:
      LCS.append(str2[LCS[-1]+1:].find(s)+1+LCS[-1])
    elif J<len(LCS):
      a = str2[LCS[j-1]+1:].find(s)
      if a != -1 and a+LCS[j-1]+1 < LCS[j]:
        LCS[j] = a+LCS[j-1]+1

print(len(LCS))
