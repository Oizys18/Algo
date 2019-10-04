import sys
sys.stdin = open('input.txt','r')
from pprint import pprint as pp

def isWall(x,y,value):
    if 0 <= x <= N-1 and 0<= y <= N-1:
        if mat[x][y] - 1 == value:return True
        else:return False
    else:return False

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def DP(x,y):
    if mat2[x][y]:
        return mat2[x][y] 
    else:
        value = mat[x][y] 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isWall(nx, ny, value):
                mat2[x][y] = DP(nx, ny) + 1
                return mat2[x][y]
        else:
            mat2[x][y] = 1
            return 1

for T in range(int(input())):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    mat2 = [[0]*N for _ in range(N)]
    score = 0
    rms = []
    for x in range(N-1,-1,-1):
        for y in range(N):
            temp = DP(x,y)
            if temp >= score:
                if temp > score:
                    rms = []
                score = temp
                rms.append(mat[x][y])
    print("#{} {} {}".format(T+1, min(rms), score)) 
