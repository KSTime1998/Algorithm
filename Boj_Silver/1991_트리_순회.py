# 1991 - 트리 순회 (Silver 1) - 많이 배웠다!
import sys
node = {}
N = int(sys.stdin.readline())
for _ in range(N):
  root, left, right = map(str,sys.stdin.readline().split())
  node[root] = [left,right]

leftside = mid = rightside = ''
def L(root):
  global leftside
  leftside += root
  left = node[root][0]
  right = node[root][1]
  if left != '.':
    L(left)
  if right != '.':
    L(right)

def M(root):
  global mid
  left = node[root][0]
  right = node[root][1]
  if left != '.':
    M(left)
  mid += root
  if right != '.':
    M(right)

def R(root):
  global rightside
  left = node[root][0]
  right = node[root][1]
  if left != '.':
    R(left)
  if right != '.':
    R(right)
  rightside += root

L('A')
M('A')
R('A')
print(leftside,mid,rightside,sep='\n')
