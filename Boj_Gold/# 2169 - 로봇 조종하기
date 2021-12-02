# 2169 - 로봇 조종하기 (Gold 1) - 넘모 어려웠다...
import sys
N,M = map(int,sys.stdin.readline().split())
region = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 왼쪽에서 온 값 : 0 , 내려온 값 : 1, 오른쪽에서 온 값 : 2
mn = -100000001
sum_value = [[[mn,mn,mn] for _ in range(M)] for _ in range(N)]

# 1층의 모든 값은 시작(위쪽에서 온다고 가정) 빼고는 왼쪽에서 오게 되어있음.
sum_value[0][0][1] = region[0][0]
for m in range(1,M):
  sum_value[0][m][1] = max(sum_value[0][m-1]) + region[0][m]

# for n in range(1,N):
for n in tqdm(range(1,N)):
  for m in range(M):
    # 내려오기 값 = 위층의 최댓값 + 지역값
    sum_value[n][m][1] = max(sum_value[n-1][m]) + region[n][m]
  # 왼쪽/오른쪽 두번째면 가장 왼쪽/가장 오른쪽의 내려오기 값 + 지역값이 왼쪽/오른쪽 값이 된다.
  sum_value[n][1][0] = sum_value[n][0][1] + region[n][1]
  sum_value[n][-2][2] = sum_value[n][-1][1] + region[n][-2]
  for m in range(2,M):
    # 왼쪽 2번째 칸부터, 자신의 칸의 한 칸 왼쪽 칸에서, 오른쪽의 경우를 제외한 값의 최댓값을 왼쪽최댓값으로 한다.
    sum_value[n][m][0] = max(sum_value[n][m-1][:2]) + region[n][m]
    # 오른쪽 2번째 칸부터, 자신의 칸의 한 칸 오른쪽 칸에서, 왼쪽의 경우를 제외한 값의 최댓값을 오른쪽최댓값으로 한다.
    sum_value[n][-m-1][2] = max(sum_value[n][-m][1:]) + region[n][-m-1]

print(max(sum_value[N-1][M-1]))
