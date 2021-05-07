# 토마토
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ7576.txt', 'r')
from collections import deque
M,N = map(int,input().split())
box = [[*map(int,input().split())] for _ in range(N)]
ripe = set()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def isUnripe(x,y):
    return 0<=x<N and 0<=y<M and box[x][y] == 0 
    
for x in range(N):
    for y in range(M):
        if box[x][y]==1:
            ripe.add((x,y))

def goRipe():
    while dq:
        x,y,d = dq.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if isUnripe(nx,ny) and not box[nx][ny]:
                box[nx][ny] = 1 
                dq.append((nx,ny,d+1))
    flag = 0 
    for x in range(N):
        for y in range(M):
            if not box[x][y]:
                flag = 1 
    if flag:
        print(-1)
    else:
        print(d)

dq = deque()
for x,y in ripe:
    dq.append((x,y,0))
goRipe()
