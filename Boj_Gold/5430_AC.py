# 5430 - AC (Gold 5) - 개행문자 주의
import sys
T = int(sys.stdin.readline())
for _ in range(T):
  p = sys.stdin.readline().rstrip()
  n = int(sys.stdin.readline())
  array = sys.stdin.readline().rstrip()[1:-1].split(',')
  delete_num = 0
  back = n
  reverse = 1
  for cmd in p:
    if cmd == 'R':
      reverse *= -1
    else:
      delete_num += 1
      if delete_num > n:
        print('error')
        break
      if reverse == -1:
        back -= 1
  if delete_num <= n:
    ans = array[delete_num-(n-back):back]
    if reverse == -1:
      ans.reverse()
    print('['+','.join(ans)+']')
