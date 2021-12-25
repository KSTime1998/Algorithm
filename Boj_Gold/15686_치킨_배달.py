# 15686 - 치킨 배달 (Gold 5)
import sys
N,M = map(int,sys.stdin.readline().split())
city = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):
  for j in range(N):
    if city[i][j] == 2:
      chicken.append((i,j))
    elif city[i][j] == 1:
      house.append((i,j))

chicken_distance = []
for i in range(len(house)):
  chicken_distance.append([])
  for j in range(len(chicken)):
    chicken_distance[-1].append((abs(house[i][0]-chicken[j][0]) + abs(house[i][1]-chicken[j][1]),j))
  chicken_distance[-1].sort(key = lambda x: x[0])

ans = 1000000000
def city_chicken_distance():
  global ans
  a = 0
  for i in chicken_distance:
    for j in i:
      if j[1] in survived:
        a += j[0]
        break
    if a >= ans:
      return
  ans = min(ans,a)

def open(M,n):
  if M == 0:
    city_chicken_distance()
  for i in range(n,len(chicken)):
    if i not in survived:
      survived.add(i)
      open(M-1,i+1)
      survived.remove(i)

survived = set()
open(M,0)

print(ans)
