#SWEA4615 
# W = 2
# B = 1 

import sys
from pprint import pprint
sys.stdin = open('input2.txt','r')

def isStone(x, y):
    if (x < N + 1 and x > 0) and (y < N + 1 and y > 0):
        if mat[x][y] != 0:
            return True
        else:
            return False
    else:
        return False

def stone(y, x, color):
    dx = [0,0,1,-1,1,-1,1,-1]
    dy = [-1,1,0,0,1,-1,-1,1]
    mat[x][y] = color
    temp = []
    if color == 1:
        for i in range(8):
            newX = x + dx[i]
            newY = y + dy[i]
            if isStone(newX, newY):
                if mat[newX][newY] == 2:
                    temp.append((newX,newY))
                    while True:
                        newX += dx[i]
                        newY += dy[i]
                        if isStone(newX, newY):
                            if mat[newX][newY] == 1:
                                break
                            elif mat[newX][newY] == 2:
                                temp.append((newX,newY))
                            elif mat[newX][newY] == 0:
                                temp = []
                                break
                        else:
                            break
                    for xx,yy in temp:
                        mat[xx][yy] = 1

    # 백돌 
    elif color == 2:
        for i in range(8):
            newX = x + dx[i]
            newY = y + dy[i]
            if isStone(newX, newY):
                if mat[newX][newY] == 1:
                    temp.append((newX,newY))
                    while True:
                        newX += dx[i]
                        newY += dy[i]
                        if isStone(newX, newY):
                            if mat[newX][newY] == 2:
                                break
                            elif mat[newX][newY] == 1:
                                temp.append((newX,newY))
                            elif mat[newX][newY] == 0:
                                temp = []
                                break
                        else:
                            break
                    for xx,yy in temp:
                        mat[xx][yy] = 2
    

for T in range(int(input())):
    N, M = map(int,input().split())
    mat = [[0]*(N+1) for _ in range(N+1)]
    md = N//2
    mat[md][md] = 2
    mat[md+1][md+1] = 2
    mat[md+1][md] = 1
    mat[md][md+1] = 1
    pprint(mat)

    for _ in range(N):
        a,b,c = map(int,input().split())
        stone(a,b,c)
        pprint(mat)
    
    B = 0
    W = 0
    for x in range(N):
        for y in range(N):
            if mat[x][y] == 2:
                W += 1
            elif mat[x][y] == 1:
                B += 1
    print("#{0} {1} {2}".format(T+1,B,W))

