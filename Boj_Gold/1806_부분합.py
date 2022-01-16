# 1806 - 부분합 (Gold 4)
# 길이 N짜리 수열 (각각의 값은 10,000 이하)
# 연속된 부분합이 S(0<S<=100,000,000) 이상이 되는 것 중 가장 짧은 것
# 불가능하면 0 출력
import sys
N,S = map(int,sys.stdin.readline().split())
number = list(map(int,sys.stdin.readline().split()))
ans = N+1

left = right = val = 0
while True:
  if val >= S:
    ans = min(ans, right-left)
    val -= number[left]
    left += 1

  elif right == N:
    break

  else:
    val += number[right]
    right += 1

if ans == N+1:
  print(0)
else:
  print(ans)
