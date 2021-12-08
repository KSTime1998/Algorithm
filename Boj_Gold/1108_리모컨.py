# 1107 - 리모컨 (Gold 5)
N = int(input())
M = int(input())
button = [0,1,2,3,4,5,6,7,8,9]

# M이 0이면 br을 받지 않고 button_n0은 [1,2,3,4,5,6,7,8,9]로 해준다.
# M이 0이 아니면 br을 받고 button과 button_n0을 만들어준다.
if M != 0:
  br = list(map(int, input().split()))
  
  # 고장난 버튼을 버튼 목록에서 제외한다.
  for i in range(M):
    button.remove(br[i])

  # button 에는 0이 있을 수 있지만, button_n0 에는 0이 있을 수 없다.
  if 0 in br:
    button_n0 = button
  else:
    button_n0 = [1,2,3,4,5,6,7,8,9]
    for i in br:
      button_n0.remove(i)

elif M == 0:
  button_n0 = [1,2,3,4,5,6,7,8,9]

# N의 자릿수
l = len(str(N))

# 만약 button_n0 == [] 일 경우, 숫자를 만들지 않고 바로 아래로 넘어간다.
if button_n0 == []:
  if button == []:
    print(abs(N-100))
  elif button == [0]:
    ch_cnt= abs(N-100)
    cnt = abs(1+N)
    if cnt > ch_cnt:
      print(ch_cnt)
    else:
      print(cnt)

else:
  # N이 l자리 수일 때, l+1자리 수 중 가장 작은 수를 만든다.
  # 당연히 가장 큰 자릿수가 0이 될 수는 없으므로 가장 큰 자릿수에 대해서는 button_n0 리스트를 이용한다.
  mx = 0
  for i in range(l+1):
    if i == l:
      mx += min(button_n0)*(10**l)
    else:
      mx += min(button)*(10**i)

  # N이 l자리 수일 때, l-1자리 수 중 가장 큰 수를 만든다.
  mn = 0
  for i in range(l-1):
    mn += max(button)*(10**i)

  ### 1. 채널버튼을 이용하지 않는다.
  # 단순히 100에서 N으로 가는 횟수를 ch_cnt에 저장한다.
  ch_cnt = abs(N-100)

  ### 2. 채널버튼을 이용한다.
  # button 을 이용하여 mn과 mx 사이에서 만들 수 있는 수를 찾는다.
  for i in range(mn,mx+1):
    F = 0
    nm = str(i)
    for j in nm:
      if int(j) in button:
        continue
      # 숫자 i의 어떤 요소가 button에 없다면 그 수를 만들 수 없으므로 루프를 빠져나간다. cnt도 세지 않는다.
      else:
        F = 1
        break
    if F == 1:
      continue
    # i가 만들 수 있는 수인 경우, cnt를 ch_cnt와 비교하여 cnt가 더 작을 때 ch_cnt를 cnt로 바꿔준다.
    else:
      cnt = len(nm)+abs(N-i)
      if ch_cnt > cnt:
        ch_cnt = cnt

  print(ch_cnt)
