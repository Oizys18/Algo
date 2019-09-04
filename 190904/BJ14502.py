from itertools import combinations
from pprint import pprint
import sys
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
    
def BFS(x, y,zeros,mat):
    queue = []
    visited = [[0]*X for _ in range(Y)]
    queue.append((x,y))
    block = list(combinations(zeros, 3))
    for b in block:
        for x, y in b:
            mat[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        if not visited[x][y]:
            visited[x][y] = 1
            mat[x][y] = 2
            for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
                newX = x + dx
                newY = y + dy
                if isPath(newX, newY):
                    queue.append((newX,newY))
    cntZ = 0
    for x1 in range(X):
        for y1 in range(Y):
            if mat[x1][y1] == 0:
                cntZ += 1
    return cntZ
    

mat = [list(map(int,input().split())) for _ in range(X)]
pprint(mat)
zeros = []
virus = []
for x in range(X):
    for y in range(Y): 
        if mat[x][y] == 0:
            zeros.append((x,y))
        elif mat[x][y] == 2:
            virus.append((x,y))

for vx, vy in virus:
    BFS(vx, vy, zeros, mat)


