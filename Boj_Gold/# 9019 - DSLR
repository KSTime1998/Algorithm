# 9019 - DSLR (Gold 5) - 배울 게 많은 문제
def D(x):
  x *= 2
  if x > 9999:
    return x % 10000
  return x

def S(x):
  if x == 0:
    return 9999
  return x -1

def L(x):
  return x//1000 + (x%1000)*10

def R(x):
  return (x%10)*1000 + x//10

for _ in range(int(input())):
  A,B = map(int,input().split())
  numberspace = [0 for _ in range(10001)]
  NUM = [[[A,'']]]
  while A >= 0:
    num = []
    for a in NUM[-1]:
      n = a[0]
      d = D(n)
      s = S(n)
      l = L(n)
      r = R(n)
      if numberspace[d] == 0:
        numberspace[d] = 1
        num.append([d,a[1]+'D'])
      if numberspace[s] == 0:
        numberspace[s] = 1
        num.append([s,a[1]+'S'])
      if numberspace[l] == 0:
        numberspace[l] = 1
        num.append([l,a[1]+'L'])
      if numberspace[r] == 0:
        numberspace[r] = 1
        num.append([r,a[1]+'R'])
    if numberspace[B] == 1:
      for a in NUM[-1]:
        if a[0] == B:
          print(a[1])
          A = -1
          break
    NUM.append(num)
