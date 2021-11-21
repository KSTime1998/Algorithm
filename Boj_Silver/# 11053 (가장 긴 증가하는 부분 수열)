# 11053 - 가장 긴 증가하는 부분 수열 (Silver 2)
# 리스트 LIS의 i번째 원소 = 리스트 A의 i번째 원소를 부분수열에 포함시킬 때 그 부분수열이 가질 수 있는 최대 길이
# 당연히 LIS[0]=1이다.
# LIS[i]를 구하는 방식 : A[0]~A[i-1] 중 A[i]보다 작은 모든 원소의 LIS값을 리스트 lis에 저장하고, LIS=max(lis)+1로 한다. 여기서 만약 len(lis)=0이면(=A[i]가 앞선 모든 원소보다 작을 때) LIS[i]=1이다.  
N=int(input())
A=list(map(int,input().split()))
LIS=[1]

for i in range(1,len(A)):
  lis=[]
  for j in range(0,i):
    if A[i]>A[j]:
      lis.append(LIS[j])
    else:
      continue
  if len(lis)==0:
    LIS.append(1)
  else:
    LIS.append(max(lis)+1)

print(max(LIS))
