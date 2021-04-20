import sys
sys.stdin = open('BOJ18500.txt','r')
from pprint import pprint as pp
from collections import deque

def isMineral(x,y):
    if 0 <= x < R and 0 <= y < C and mat[x][y]!=0:return True

def isMap(x,y):
    if 0 <= x < R and 0 <= y < C: return True 

def getCluster():
    cluster = 0
    floating = {}
    visit = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if mat[x][y] and not visit[x][y]:
                isLanded = 0
                cluster += 1        
                queue = deque()
                temp_float = deque()
                queue.appendleft((x,y))
                temp_float.appendleft((x,y))
                visit[x][y] = 1
                while queue:
                    x,y = queue.popleft()
                    mat[x][y] = cluster
                    if (x,y) not in temp_float:
                        temp_float.appendleft((x,y))
                    if x == R-1:isLanded = 1
                    for i in range(4):
                        nx,ny = x+dx[i], y+dy[i]
                        if isMineral(nx,ny) and not visit[nx][ny]:
                            queue.appendleft((nx,ny))
                            visit[nx][ny] = 1
                if not isLanded:
                    # floating.append(cluster)
                    floating[cluster] = temp_float
    return floating

def throw(stone,i):
    x = R - stone
    if i%2: # 1,3,5,7 ... <-
        for y in range(C-1,-1,-1):
            if mat[x][y]:
                mat[x][y] = 0
                return  
    else: # 0,2,4,6 ... ->  
        for y in range(C):
            if mat[x][y]:
                mat[x][y] = 0
                return 

def drop(falling):
    
    far = 1
    flag = 0
    while not flag:
        for x,y in falling:
            if (x+far,y) in falling:
                continue
            if not isMap(x+far,y) or (isMineral(x+far,y) and (x+far,y) not in falling):
                flag = 1
        if not flag:
            far += 1
    for x,y in falling:
        mat[x+far-1][y],mat[x][y] = mat[x][y],0

R,C = map(int,input().split())
mat = [[0 if i=='.' else 1 for i in input() ] for _ in range(R)]

N = int(input())
stones = list(map(int,input().split()))

# direction
dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(len(stones)):
    throw(stones[i],i)
    floating = getCluster()
    while len(floating.keys()):
        for cluster in floating.keys():
            falling = floating[cluster]
            drop(falling)
        floating = getCluster()

for x in range(R):
    print(''.join(['x' if mat[x][y] else '.' for y in range(C)]))