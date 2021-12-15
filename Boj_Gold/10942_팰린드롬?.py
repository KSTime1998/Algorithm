# 10942 - 팰린드롬? (Gold 3)
import sys
N = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))

palindrome_index = set()
def palindrome(left,right):
  while left >= 0 and right < N:
    if number[left] == number[right]:
      palindrome_index.add((left,right))
      left -= 1
      right += 1
    else:
      break

for i in range(1,N):
  if number[i] == number[i-2]:
    palindrome_index.add((i-2,i))
    palindrome(i-3,i+1)
  if number[i] == number[i-1]:
    palindrome_index.add((i-1,i))
    palindrome(i-2,i+1)

ans = []
for _ in range(int(sys.stdin.readline())):
  S,E = map(int,sys.stdin.readline().split())
  if S==E or (S-1,E-1) in palindrome_index:
    ans.append(1)
  else:
    ans.append(0)
print('\n'.join(map(str,ans)))
