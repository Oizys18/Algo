import sys
sys.stdin = open('input6.txt','r')
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
from pprint import pprint


def isLand(x, y):
    if (x >= 0 and x <= N-1) and (y >= 0 and y <= N-1):
        return True
    else:
        return False


mat2 = [[0]*N for _ in range(N)]  
def BFS(x, y):
    global mat2
    queue = []
    queue.append((x,y))
    Lnd = 1
    while queue:
        x,y = queue.pop(0)
        if mat2[x][y] == 0:
            mat2[x][y] = 1
            Lnd += 1
            for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
                newX = x + dx
                newY = y + dy
                if isLand(newX,newY) and mat[newX][newY] != 0:
                    queue.append((newX,newY))     
    return Lnd

def flood():
    for x in range(N):
        for y in range(N):
            if mat[x][y] <= level:
                mat[x][y] = 0
    
level = 1
preCnt = 1

while True: 
    # land의 갯수를 센다 
    flood()
    cnt = 0
    for x in range(N):
        for y in range(N):
            if mat[x][y] and mat2[x][y] == 0:
                if BFS(x,y):
                    cnt += 1
    if cnt > preCnt:
        preCnt = cnt 
    if cnt == 0:
        print(preCnt)
        break

    # 물 붓기 1씩 
    level += 1 
    mat2 = [[0]*N for _ in range(N)]  
    