# 2579 - 계단 오르기 (Silver 3)
import sys
N = int(sys.stdin.readline())
# stair : stair[i]는 i번째 계단의 값을 나타낸다.
stair = list((int(sys.stdin.readline()) for i in range(N)))
stair.insert(0,0)
# val : val[i]는 i번째 계단까지 갈 때 얻을 수 있는 최댓값을 나타낸다.
val = [0]
val.append(stair[1])
if N == 1 :
  print(val[1])
else:
  val.append(stair[1]+stair[2])
  if N == 2:
    print(val[2])
  else:
    # i번째 계단의 값 = str[i] + val[i-1] or str[i] + val[i-2]
    # 만약 전자를 택했다면 i+1번째에서는 전자를 택할 수 없다.
    # 이를 프로그래밍 언어로 표현하면 i번째 이후의 어떤 val[x]에서 str[i+1]+val[i]를 취하는 경우가 없어야 함.
    # 그렇지만 val[x]가 str[x-1]을 취하는 경우는 가능해야 함.
    # val[i] = str[i]+str[i-1]+val[i-3] or str[i]+val[i-2] 라고 하면 됨.
    ## 마지막 계단은 무조건 밟아야 함. 이건 계단 순서대로 전부 연산하니 자동적으로 충족됨.
    for i in range(3,N+1):
      val.append(max(stair[i]+stair[i-1]+val[i-3] , stair[i]+val[i-2]))

    print(val[N])
