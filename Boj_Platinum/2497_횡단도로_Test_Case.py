from random import randrange
from time import time
from tqdm import tqdm
import matplotlib.pyplot as plt

# N = 5
# city = [[3,7],[5,6],[4,0],[2,2],[1,5]]
# 3 7 2 2

# N = 4
# city = [[1,1],[1,0],[0,0],[0,1]]
# 1 1 0 0

# 랜덤 최대 케이스
# n = 75
# city = []
# c = set()
# while len(c) < n:
#   x = randrange(1500,2000)
#   y = randrange(2001-x,x)
#   c.add((x,y))
# c = sorted(list(c), key = lambda x : x[1],reverse=True)
# city += c
# c = set()
# while len(c) < n:
#   y = randrange(0,501)
#   x = randrange(y,2001-y)
#   c.add((x,y))
# c = sorted(list(c), key = lambda x : x[0],reverse=True)
# city += c
# c = set()
# while len(c) < n:
#   x = randrange(0,501)
#   y = randrange(x,2001-x)
#   c.add((x,y))
# c = sorted(list(c), key = lambda x : x[1])
# city += c
# c = set()
# while len(c) < n:
#   y = randrange(1500,2001)
#   x = randrange(2001-y,y)
#   c.add((x,y))
# c = sorted(list(c), key = lambda x : x[0])
# city += c
# N = 4*n
# print(city)

# 테케 2. 통과!
# N = 10
# city = [[5,10],[7,10],[8,8],[7,6],[5,3],[3,3],[2,4],[3,6],[4,7],[5,8]]
# 7 10 7 6

# N = 7
# city = [[0,3],[4,8],[9,7],[10,4],[6,3],[10,1],[5,0]]
# 4 8 5 0

# N = 8
# city = [[3,0],[1,1],[0,3],[2,5],[3,5],[5,5],[6,3],[4,2]]
# 3 0 2 5  - 스페셜 저지


# N = 10
# city = [[9,41],[31,119],[95,122],[122,124],[181,179],[194,142],[177,62],[116,75],[69,31],[33,16]]
# city = [[69,31],[33,16],[9,41],[31,119],[95,122],[122,124],[181,179],[194,142],[177,62],[116,75]]
# 9 41 95 122

# N = 15
# city = [[82,169],[114,185],[172,154],[197,161],[176,60],[184,24],[123,136],[104,91],[89,12],[82,128],[51,41],[40,31],[33,84],[24,150],[39,193]]
# 82 169 82 128

# N = 4
# city = [[0,0],[0,1],[1,1],[2,0]]
# 0 1 2 0

x = [i[0] for i in city]
y = [i[1] for i in city]
print(x,y)
plt.scatter(x,y)
plt.grid(True)
