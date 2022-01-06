# 2263 - 트리의 순회 (Gold 2)
import sys
sys.setrecursionlimit(10**6)
freeorder = []
in_index = {}
for i in range(n):
  in_index[inorder[i]] = i

def findtree(s1,e1,s2,e2):
  if e1 >= s1 and e2 >= s2:
    root = postorder[e2]
    freeorder.append(root)
    m = in_index[root]
    L = m - s1
    findtree(s1,m-1,s2,s2+L-1)
    findtree(m+1,e1,s2+L,e2-1)

findtree(0,n-1,0,n-1)
print(' '.join(map(str,freeorder)))
