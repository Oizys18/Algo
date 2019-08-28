# SWEA 4875 미로
import sys
sys.stdin = open('input3.txt','r')

def isPath(x,y):
    if (x <= N - 1 and x >= 0) and (y <= N -1 and y >= 0): 
        if mat[x][y] == '0' or mat[x][y] == '3':
            return True
        elif mat[x][y] == '1':
            return False
    else:
        return False 


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bt(x,y):
    stack = []
    visited = []
    stack.append((x,y))
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            x = node[0]
            y = node[1]
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                if isPath(newX,newY):
                    stack.append((newX,newY))
                    if mat[newX][newY] == '3':
                        return 1 
    return 0

for T in range(int(input())):
    N = int(input())
    mat = [input() for _ in range(N)]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '2':
                start = (i,j)
    print("#{0} {1}".format(T+1,bt(start[0],start[1])))
    
