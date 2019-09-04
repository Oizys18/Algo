from itertools import combinations
from pprint import pprint
import sys, copy
sys.stdin = open('input4.txt','r')

X, Y = map(int,input().split())

def isPath(x, y):
    if (x >= 0 and x <= X-1) and (y >= 0 and y <= Y-1):
        if mat[x][y] == 0:
            return True
        else:
            return False 
    else:
        return False
    
def BFS(x, y):
    queue = []
    queue.append((x,y))
    test[x][y] = 0
    while queue:
        x, y = queue.pop(0)
        if test[x][y] == 0:
            test[x][y] = 2
            for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
                newX = x + dx
                newY = y + dy
                if isPath(newX, newY):
                    queue.append((newX,newY))
    # pprint(mat)

mat = [list(map(int,input().split())) for _ in range(X)]
zeros = []
virus = []
ones = []

for x in range(X):
    for y in range(Y): 
        if mat[x][y] == 0:
            zeros.append((x,y))
        elif mat[x][y] == 2:
            virus.append((x,y))
        elif mat[x][y] == 1:
            ones.append((x,y))
test = [[0]*Y for _ in range(X)]
for x,y in ones:
    test[x][y] = 1
res = 0
for dots in list(combinations(zeros, 3)):
    for a,b in dots:
        test[a][b] = 1    
    for x,y in virus:
        BFS(x,y)
    cntZ = 0
    for x1 in range(X):
        for y1 in range(Y):
            if test[x1][y1] == 0:
                cntZ += 1
    if cntZ > res:
        res = cntZ
    test = [[0]*Y for _ in range(X)]
    for x,y in ones:
        test[x][y] = 1
print(res)





# res = 0
# for b in block:
#     for l,m in b:
#         mat[l][m] = 1
#     pprint(mat)
#     pprint(matOri)
#     print(' ')
#     for vx, vy in virus:
#         BFS(vx, vy)
#     pprint(mat)
#     cntZ = 0
#     for x1 in range(X):
#         for y1 in range(Y):
#             if mat[x1][y1] == 0:
#                 cntZ += 1
#     if cntZ > res:
#         res = cntZ
#     #     # pprint(mat)

#     for l,m in b:
#         mat[l][m] = 0
#     mat = copy.deepcopy(matOri)
# print(res)

