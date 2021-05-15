import sys
sys.stdin = open('BOJ2638.txt','r')
from pprint import pprint as pp 
from collections import deque

N,M = map(int,input().split())
mat = [[*map(int,input().split())] for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def isMap(x,y):
    return 0<=x<N and 0<=y<M

def check_outside(x,y):
    q = deque()
    q.append((x,y))
    visit = [[0]*M for _ in range(N)]
    visit[x][y] = 1
    empty = set()
    outer = set()
    while q:
        x,y = q.popleft()
        empty.add((x,y))
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if isMap(nx,ny) and not visit[nx][ny] and not mat[nx][ny]:
                visit[nx][ny] = 1 
                q.append((nx,ny))
            elif isMap(nx,ny) and mat[nx][ny]:
                outer.add((nx,ny))

    return empty,outer

empty,outer = check_outside(0,0)
time = 0
while outer:
    melt = set()
    for x,y in outer:
        cnt = 0
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if isMap(nx,ny) and not mat[nx][ny] and (nx,ny) in empty:
                
                cnt += 1 
        if cnt >= 2:
            melt.add((x,y))
    for x,y in melt:
        mat[x][y] = 0 
    empty,outer = check_outside(0,0)
    time += 1 
    
print(time)