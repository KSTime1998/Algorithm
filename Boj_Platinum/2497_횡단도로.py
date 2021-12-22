# 2497 - 횡단도로 (Platinum 4)
import sys
N = int(sys.stdin.readline())
city = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def f(c1,c2):
  x1,y1 = city[c1][0],city[c1][1]
  x2,y2 = city[c2][0],city[c2][1]
  return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

length = [f(i,i-1) for i in range(N)]
round = sum(length)

c1_to_c2 = [[0 for _ in range(N)] for i in range(N)]
sorted_length = []
for i in range(N):
  leftway = 0
  rightway = round
  for j in range(i+1,N):
    leftway += length[j]
    rightway -= length[j]
    if leftway < rightway:
      c1_to_c2[i][j] = leftway
      c1_to_c2[j][i] = leftway
      sorted_length.append([leftway,i,j])
    else:
      c1_to_c2[i][j] = rightway
      c1_to_c2[j][i] = rightway
      sorted_length.append([rightway,i,j])
sorted_length = sorted(sorted_length, key = lambda x : -x[0])

C1 = sorted_length[0][1]
C2 = sorted_length[0][2]
min_maxlength = sorted_length[0][0]
min_maxcity = [city[C1][0],city[C1][1],city[C2][0],city[C2][1]]

def crosslength(c1,c2):
  global min_maxlength,min_maxcity
  cross = f(c1,c2)
  maxlength = 0
  for i in range(0,len(sorted_length)):
    x,y = sorted_length[i][1],sorted_length[i][2]
    if c1 == x:
      node_minlength = min(sorted_length[i][0],cross + c1_to_c2[c2][y])
    elif c2 == x:
      node_minlength = min(sorted_length[i][0],cross + c1_to_c2[c1][y])
    elif c1 == y:
      node_minlength = min(sorted_length[i][0],cross + c1_to_c2[x][c2])
    elif c2 == y:
      node_minlength = min(sorted_length[i][0],cross + c1_to_c2[x][c1])
    else:
      x_c1_c2_y = c1_to_c2[x][c1] + cross + c1_to_c2[c2][y]
      x_c2_c1_y = c1_to_c2[x][c2] + cross + c1_to_c2[c1][y]
      node_minlength = min(sorted_length[i][0],x_c1_c2_y,x_c2_c1_y)
    maxlength = max(maxlength,node_minlength)
    if sorted_length[i][0] == node_minlength or maxlength >= min_maxlength:
      break

  if maxlength < min_maxlength:
    min_maxlength = maxlength
    min_maxcity = [city[c1][0],city[c1][1],city[c2][0],city[c2][1]]

for c1 in range(0,N-1):
  for c2 in range(c1+2,N):
    crosslength(c1,c2)

print(' '.join(str(i) for i in min_maxcity))
