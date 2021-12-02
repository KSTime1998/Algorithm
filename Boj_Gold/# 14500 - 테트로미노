# 14500 - 테트로미노 (Gold 5) - max(map(max,space)) 배움
# 테트로미노의 모양을 신경 쓸 필요는 없다. --- 사실 있었음.
import sys
N,M = map(int,sys.stdin.readline().split())
space = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

D = [[1,0],[0,1],[-1,0],[0,-1]]
ans = 0
maxval = max(map(max,space))

# 테트로미노 구성 원리 : 이미 지나간 점은 지나가지 않게 하고(가능한 방향은 처음을 제외하고 최대 3방향임) 모든 경우로 뻗어나가면 됨.
# 그러나 그냥 쭉 뻗어나가게 구성하면 T 모양 테트로미노를 만들 수 없다.
# 두 번째 점에서 세 번째 점을 선택했을 때, 마지막 점을 다시 두 번째 점에서 택하는 경우를 추가하면 T를 만들 수 있다.
# ***** 만약 (현재까지의 값) + (space의 최댓값 * 고를 수 있는 남은 점의 수) <= 지금 결정되어있는 최댓값이라면 더 볼 필요도 없음.
def tetromino(x,y,last_visited,stack,value):
  global ans
  if value + maxval * (4-stack) <= ans:
    return
  for d in D:
      X = x + d[0]
      Y = y + d[1]
      if [X,Y] not in last_visited and 0 <= X < N and 0 <= Y < M:
        val = value+space[X][Y]
        if stack == 3:
          ans = max(ans,val)
        else:
          tetromino(X,Y,last_visited+[[X,Y]],stack+1,val)
          if stack == 2:
            tetromino(x,y,last_visited+[[X,Y]],stack+1,val)

for i in tqdm(range(N)):
  for j in range(M):
    tetromino(i,j,[[i,j]],1,space[i][j])

print(ans)
