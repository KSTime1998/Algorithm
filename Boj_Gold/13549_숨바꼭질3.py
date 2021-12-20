# 13549 - 숨바꼭질 3 (Gold 5)
import sys
N,K = map(int,sys.stdin.readline().split())
maxpoint = 100001

if N == K:
  print('0')
else:
  visited = [0]*(maxpoint)
  visited[N] = 1
  visit = [N]
  left = T = 0
  arrive = False
  right = 1
  while True:
    for i in range(left,right):
      p = visit[i]
      if p != 0:
        while p < K and p <= 50000:
          p *= 2
          if visited[p] == 0:
            visited[p] = 1
            visit.append(p)
          if p == K:
            arrive = True
            break
      if arrive:
        break
    if arrive:
      break

    T += 1
    right = len(visit)
    for i in range(left,right):
      p = visit[i]
      if p < K:
        j = p+1
        if j == K:
          arrive = True
          break
        if visited[j] == 0:
          visited[j] = 1
          visit.append(j)

      if p > 0:
        j = p-1
        if j == K:
          arrive = True
          break
        if visited[j] == 0:
          visited[j] = 1
          visit.append(j)

    if arrive:
      break
    left = right
    right = len(visit)

  print(T)
