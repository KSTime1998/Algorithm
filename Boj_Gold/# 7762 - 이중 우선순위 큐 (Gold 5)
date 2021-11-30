# 7762 - 이중 우선순위 큐 (Gold 5) - heapq 사용...
import sys
import heapq

T = int(sys.stdin.readline())

def delete(h):
  while h != [] and h[0][1] not in key:
    heapq.heappop(h)

for _ in range(T):
  mxh, mnh = [], []
  k = int(sys.stdin.readline())
  key = set()
  for i in range(k):
    c1, c = sys.stdin.readline().split()
    c = int(c)

    if c1 == 'I':
      key.add(i)
      heapq.heappush(mxh, (-c,i))
      heapq.heappush(mnh, (c,i))
    else:
      if c == 1:
        delete(mxh)
        if mxh != []:
          key.remove(mxh[0][1])
          heapq.heappop(mxh)

      else:
        delete(mnh)
        if mnh != []:
          key.remove(mnh[0][1])
          heapq.heappop(mnh)

  delete(mxh)
  delete(mnh)
  if mxh and mnh :
    print(-mxh[0][0],mnh[0][0],sep=' ')
  else:
    print("EMPTY")
