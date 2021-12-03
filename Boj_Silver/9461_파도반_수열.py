# 9461 - 파도반 수열 (Silver 3)
T = int(input())

# 삼각형 하나가 추가되면 60도 회전한다. 따라서 어떤 삼각형이 만들어지고 6번째 뒤의 삼각형이 같은 위상을 갖는다.
# 따라서 6번째 항부터 P(N)은 직전 항과 다섯 번째 전 항의 합이다. 
P_N = [0,1,1,1,2,2]

for i in range(T):
  N = int(input())
  if len(P_N)-1 < N:
    for i in range(len(P_N),N+1):
      P_N.append(P_N[i-1]+P_N[i-5])
  print(P_N[N])
