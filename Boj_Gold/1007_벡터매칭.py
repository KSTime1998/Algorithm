# 1007 - 벡터 매칭 (Gold 2)
# 결국 벡터를 어떻게 만들든, 시작점 값은 더해지고 도착점 값은 빼지므로 그것만 보면 된다.
import sys
T = int(sys.stdin.readline())

# 10개에 1을 5개 집어넣는 경우의 수 =
#1번째에 1을 넣고 9개에 1을 4개 집어넣는 경우의 수 + 1번째에 안 넣고 9개에 1개를 5개 집어넣는 경우의 수 
def length(num,cnt):
  global ans
  if num == N:
    return
  if cnt == N//2:
    x = y = 0
    for i in range(N):
      if c[i] == 1:
        x += P[i][0]
        y += P[i][1]
      else:
        x -= P[i][0]
        y -= P[i][1]
    if d(x,y) < ans:
      ans = d(x,y)
    return
  
  else:
    c[num] = 1
    length(num+1,cnt+1)
    c[num] = 0
    length(num+1,cnt)

def d(x,y):
  return (x**2 + y**2)**(1/2)

for i in range(T):
  ans = 10**20
  N = int(sys.stdin.readline())
  P = []
  for j in range(N):
    P.append(list(map(int,sys.stdin.readline().split())))
  c = [0 for i in range(N)]
  length(0,0)
  print(ans)
