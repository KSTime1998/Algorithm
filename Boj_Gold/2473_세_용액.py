# 2473 - 세 용액 (Gold 4)
import sys

N = int(sys.stdin.readline())
solution = sorted(list(map(int,sys.stdin.readline().split())))
ans = [solution[i] for i in range(3)]
minval = abs(sum(solution[i] for i in range(3)))
left = 0
right = len(solution)-1

for left in range(N-2):
  mid = left + 1
  right = N - 1

  while right > mid:
    val = solution[left] + solution[mid] + solution[right]

    if minval > abs(val):
      minval = abs(val)
      ans = [solution[left],solution[mid],solution[right]]

    if val > 0:
      right -= 1
    elif val == 0:
      break
    else:
      mid += 1

print(' '.join(map(str,ans)))
