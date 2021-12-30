# 9935 - 문자열 폭발 (Gold 4)
import sys
string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = []
last = bomb[-1]
l2 = len(bomb)

for s in string:
  stack.append(s)
  if s == last:
    if ''.join(stack[-l2:]) == bomb:
      del stack[-l2:]
if stack == []:
  print("FRULA")
else:
  print(''.join(stack))
