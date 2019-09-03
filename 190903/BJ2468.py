import sys
sys.stdin = open('input6.txt','r')
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
def isLand(x,y):
    if (x >= 0 and x <= N-1) and (y >= 0 and y <= N-1):
        if mat[x][y]:
            return True
        else:
            return False
    else:
        return False

def BFS(x, y):
    mat2 = [[0]*N for _ in range(N)]
    queue = []
    while queue:
        if mat2[x][y] == 0:
            mat2[x][y] = 1
            for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
                newX = x + dx
                newY = y + dy
                if isLand(newX,newY):
                    queue.append((x,y))
                



while True:
    flood = 1
    cnt = 0 
    for x in range(X):
        for y in range(Y):
            