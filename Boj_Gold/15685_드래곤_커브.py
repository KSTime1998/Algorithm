# 15685 - 드래곤 커브 (Gold 4)
import sys
N = int(sys.stdin.readline())

direction = [[1,0],[0,-1],[-1,0],[0,1]]
visit = set()

# 드래곤 커브를 그리고, 좌표를 저장하는 함수
for _ in range(N):
  x,y,dir,generation = map(int,sys.stdin.readline().split())

  dragon_curve_dir = [dir]
  visit.add((x,y))
  x_coord = x
  y_coord = y
  minrange = 0

  # 세대수만큼 반복
  while generation >= 0:
    maxrange = len(dragon_curve_dir)
    generation -= 1

    # dir정보에 따라 좌표를 더해가며 visit에 저장
    for i in range(minrange,len(dragon_curve_dir)):
      x_coord += direction[dragon_curve_dir[i]][0]
      y_coord += direction[dragon_curve_dir[i]][1]
      visit.add((x_coord,y_coord))

    # dir 정보 갱신
    D = []
    for i in range(1,len(dragon_curve_dir)+1):
      D.append(dragon_curve_dir[-i])
    for d in D:
      if d == 3:
        dragon_curve_dir.append(0)
      else:
        dragon_curve_dir.append(d+1)

    minrange = maxrange

#2 저장한 좌표들에서 정사각형을 찾아내는 함수
ans = 0
for i in range(0,100):
  for j in range(0,100):
    if (i,j) in visit and (i+1,j) in visit and (i,j+1) in visit and (i+1,j+1) in visit:
      ans += 1

print(ans)
