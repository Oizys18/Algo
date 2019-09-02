# 문제3 : 섬의 개수 구하기
import sys
sys.stdin = open('input3.txt','r')


def eight(x,y):
    direc = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0,1),
        (1,-1),
        (1,0),
        (1,1),
    ]
    if mat[y][x]: 
        for i in range(len(direc)):
            a, b = direc[i]
            if mat[y+b][x+a]:
                if mat[y][x] > mat[y+b][x+a]:
                    mat[y+b][x+a] = mat[y][x]
                elif mat[y+b][x+a] > mat[y][x]:
                    mat[y][x] = mat[y+b][x+a]

for T in range(1, int(input())+1):
    N = int(input())
    mat = []
    for _ in range(N):
        mat.append(list(map(int,input().split())))
    tempMat = mat
    
    while True:
        tempMat = mat
        for _ in range(N):
            for r in range(1,len(mat)-1):
                for c in range(1,len(mat)-1):
                    eight(r,c)
        if tempMat == mat:
            break
        

    island = []
    for r in mat:
        island.extend(list(set(r)))
    island = set(island)
    island.remove(0)
    result = len(island)
    print("#{0} {1}".format(T,result))
    