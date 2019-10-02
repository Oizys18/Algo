# BJ2589 보물섬

"""
depth BFS
mat2 만들어서 visited 
depth가 가장 깊은 것을 출력 
"""
import sys
from pprint import pprint
sys.stdin = open('input.txt','r')

X, Y = map(int,input().split())
# Land = 1 /// Water = 0
mat = [[1 if x=='L' else 0 for x in input()] for _ in range(X)]

def isLand(x,y):
    if (x >= 0 and x <= X-1) and (y >= 0 and y <= Y-1):
        if mat[x][y] == 1:
            return True
        else:
            return False
    else:
        return False

def BFS(depth,x,y):
    visited = [[0]*Y for _ in range(X)]
    queue = []
    queue.append((depth,x,y))
    maxD = 0
    while queue:
        depth, x, y = queue.pop(0)
        if depth > maxD:
            maxD = depth
        if not visited[x][y]:
            visited[x][y] = 1
            for dx,dy in (0,1), (0,-1), (-1,0), (1,0):
                newX = x + dx
                newY = y + dy
                if isLand(newX,newY) and not visited[newX][newY]:
                    queue.append((depth+1,newX,newY))
    return maxD

res = 0
for x in range(X):
    for y in range(Y):
        if mat[x][y]:
            md = BFS(0,x,y)
            if res < md:
                res = md     
print(res)


    