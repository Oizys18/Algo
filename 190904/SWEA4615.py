#SWEA4615 
# W = 2
# B = 1 

import sys
from pprint import pprint
sys.stdin = open('input2.txt','r')

def isStone(x, y):
    if (x < N + 1 and x > 0) and (y < N + 1 and y > 0):
        if mat[x][y]:
            return True
        else:
            return False
    else:
        return False
def stone(y, x, c):
    mat[x][y] = c
    temp = []
    if c == 1:
        cns = 2
    else:
        cns = 1
    for dx,dy in (0,-1), (0,1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1):
        newX, newY = x + dx, y + dy
        if isStone(newX, newY):
            if mat[newX][newY] == cns:
                while True:
                    if isStone(newX, newY):
                        if mat[newX][newY] == c:
                            break
                        elif mat[newX][newY] == cns:
                            temp.append((newX,newY))
                    else:
                        temp = []
                        break
                    newX += dx
                    newY += dy 
                for xx,yy in temp:
                    mat[xx][yy] = c

for T in range(int(input())):
    N, M = map(int,input().split())
    mat = [[0]*(N+1) for _ in range(N+1)]
    md = N//2
    mat[md][md] = 2
    mat[md+1][md+1] = 2
    mat[md+1][md] = 1
    mat[md][md+1] = 1
    for _ in range(M):
        a,b,c = map(int,input().split())
        stone(a,b,c)

    B = 0
    W = 0
    for x in range(1,N+1):
        for y in range(1,N+1):
            if mat[x][y] == 2:
                W += 1
            elif mat[x][y] == 1:
                B += 1
    print("#{0} {1} {2}".format(T+1,B,W))

