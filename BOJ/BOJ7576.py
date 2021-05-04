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
    return 0<=x<N and 0<=y<M and box[x][y] != -1
for x in range(N):
    for y in range(M):
        if box[x][y]==1:
            ripe.add((x,y))

def goRipe(x,y):
    dq = deque()
    dq.append((x,y))
    date = 2
    visit = [[0]*M for _ in range(N)]
    visit[x][y] = 1
    while dq:
        x,y = dq.pop()
        print(x,y,dq)
        pp(box)
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if isUnripe(nx,ny) and not visit[nx][ny]:
                visit[nx][ny] = 1
                if box[nx][ny]:
                    box[nx][ny] = min(box[nx][ny],date)
                else:
                    box[nx][ny] = date
                dq.append((nx,ny))
        date += 1

for x,y in ripe:
    goRipe(x,y)
