# 15824 - 너 봄에는 캡사이신이 맛있단다 (Gold 1)
import sys
N = int(sys.stdin.readline())
menu = list(map(int,sys.stdin.readline().split()))
menu.sort()
ans = minus = 0
n = 1
for last in range(1,N):
  # menu[0] 부터 menu[last-1]까지 총 last-1개에서 랜덤 개수만큼 뽑을 수 있다.
  # 총 조합의 수 = 2**(last) -1개.
  # 따라서 총 조합의 수 만큼 menu[last]를 더하고,
  # 가장 작은 값부터 총 조합의 수에서 //2씩 해가며 menu[해당 값]을 빼면 된다.
  ## last = 1일 때 : menu[1]*1 - menu[0]
  ## last = 2일 때 : menu[2]*3 - menu[0]*2 - menu[1]
  ## last = 3일 때 : menu[3]*7 - menu[0]*4 - menu[1]*2 - menu[2]
  ## 결국 빼는 값은 매번 계산할 필요 없이, (이전에 빼줬던 값)*2 + menu[last-1]만큼만 해주면 된다.
  minus = (minus*2 + menu[last-1])%1000000007
  n = (n*2)%1000000007
  ans += (menu[last] * (n - 1) - minus)%1000000007

print(ans%1000000007)
