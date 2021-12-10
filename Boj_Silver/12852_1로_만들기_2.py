# 12852 - 1로 만들기 2 (Silver 1)
N = int(input())
num = [0 for _ in range(N+1)]
cnt = [0 for _ in range(N+1)]

for i in range(2,N+1):
  num[i] = i-1
  cnt[i] = cnt[i-1] + 1
  if i%2 == 0 and cnt[i//2]+1 < cnt[i]:
    num[i] = i//2
    cnt[i] = cnt[i//2] + 1
  if i%3 == 0 and cnt[i//3]+1 < cnt[i]:
    num[i] = i//3
    cnt[i] = cnt[i//3]+1

ans = [N]
def printanswer(n):
  if n == 1:
    print(' '.join(str(i) for i in ans))
    return
  m = num[n]
  ans.append(m)
  printanswer(m)

print(cnt[N])
printanswer(N)
