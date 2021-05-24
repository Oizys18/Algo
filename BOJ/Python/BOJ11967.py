# Turn on Fire 
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ11967.txt', 'r')

from collections import deque

N,M = map(int,input().split())
rooms = [[0]*(N+1) for _ in range(N+1)]
signals = [[*map(int,input().split())] for _ in range(M)]
rooms[1][1] = 1 
dx = [0,0,-1,1]
dy = [-1,1,0,0]

signal_dict = dict()
for x,y,a,b in signals:
    if not signal_dict.get((x,y)):
        signal_dict[(x,y)] = []
    signal_dict[(x,y)].append((a,b))
    

def isMap(x,y):
    return 0<x<N+1 and 0<y<N+1

def check(x,y):
    q = deque()
    q.append((x,y))
    visit = [[0]*(N+1) for _ in range(N+1)]
    visit[x][y] = 1 
    cnt = 0 
    while q:
        x,y = q.popleft()
        if signal_dict.get((x,y)):
            for nx,ny in signal_dict[(x,y)]:
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    cnt += 1

        for i in range(4):
            nx,ny = x + dx[i] , y+dy[i]
            if isMap(nx,ny) and visit[nx][ny]: 
                q.append((nx,ny))

    return cnt
print(check(1,1))




# def DFS(x,y,mat):   
#     q = deque()
#     q.append((x,y))
#     check_visit = [[0]*(N+1) for _ in range(N+1)]
#     check_visit[x][y] = 1 
#     cnt = 0
#     while q:
#         x,y = q.popleft()
#         cnt += 1 
#         for i in range(4):
#             nx,ny = x + dx[i] , y+dy[i]
#             if isMap(nx,ny) and mat[nx][ny] and not check_visit[nx][ny]:
#                 check_visit[nx][ny] = 1 
#                 q.append((nx,ny))
#     return cnt 

# print(DFS(1,1,visit))

