# 16236 - 아기 상어 (Gold 4) - **********
N = int(input())
space = []

# 공간에 대한 정보를 받아 이중 리스트로 저장한다.
for i in range(N):
  space.append(list(map(int, input().split())))

# 초기 시간 0, 초기 크기 0, 그리고 eat은 먹을 때마다 1씩 증가하고 size와 값이 같아지면 0으로 초기화하며 size를 1 늘린다.
time = 0
cnt = 0
size = 2
eat = 0

# 처음 상어의 위치를 찾아 pos 리스트에 저장한다. 해당 위치의 값을 0으로 바꿔준다.
for i in range(N):
  for j in range(N):
    if space[i][j] == 9:
      pos = [[i,j]]
      space[i][j] = 0
      break

# pos 리스트에 대해 다음 루프를 실행한다.
# pos 리스트의 각 원소를 상 우 좌 하 순으로 한 칸 움직이며 탐색한다.
# 옮긴 위치가 pos에 있으면 스킵한다.
# 옮긴 위치가 space 안에 있고, 그곳의 값이 size와 같거나 0이면 path와 po(집합)에 저장한다.
# 옮긴 위치가 space 안에 있고, 그곳의 값이 size보다 작으면 그곳으로 path와 po를 옮긴다.
## 이 때 time을 cnt만큼 추가하고 eat을 1 늘린다. cnt는 0으로 초기화한다.
## eat이 size와 같아지면 eat을 0으로 바꾸고 size를 1 늘린다.
# 루프가 끝나면 pos를 po로 동기화한다. cnt를 1 늘린다.
# 루프가 끝났는데 po가 빈 집합이면 종료하고 time을 출력한다.

def eatable(i,j):
  global eata,time,cnt,eat,size,e
  if eata == 0:
    eata = 1
    e = [[i,j]]
  else:
    I,J = e[0][0],e[0][1]
    if i < I:
      e = [[i,j]]
    elif i == I and j < J:
      e = [[i,j]]

n = 0
while True:
  m = len(pos)
  cnt += 1
  eata = 0
  e = []
  x,y = pos[0][0],pos[0][1]
  for a in range(n,m):
    i = pos[a][0]
    j = pos[a][1]

    if i > 0:
      if 0 < space[i-1][j] < size :
        eatable(i-1,j)
      elif eata == 0 and space[i-1][j] <= size and [i-1,j] not in pos :
        pos.append([i-1,j])

    if j > 0:
      if 0 < space[i][j-1] < size :
        eatable(i,j-1)
      elif eata == 0 and space[i][j-1] <= size and [i,j-1] not in pos :
        pos.append([i,j-1])

    if j < N-1:
      if 0 < space[i][j+1] < size :
        eatable(i,j+1)
      elif eata == 0 and space[i][j+1] <= size and [i,j+1] not in pos :
        pos.append([i,j+1])

    if i < N-1:
      if 0 < space[i+1][j] < size :
        eatable(i+1,j)
      elif eata == 0 and space[i+1][j] <= size and [i+1,j] not in pos :
        pos.append([i+1,j])

  if eata == 1 :
    pos = e
    space[e[0][0]][e[0][1]] = 0
    eat += 1
    time += cnt
    cnt = 0
    if eat == size:
      size += 1
      eat = 0
    n = 0
  else:
    n = m
  
  if len(pos) == m and pos[0] == [x,y]:
    print(time)
    break
