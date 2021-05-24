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

pp(signal_dict)
def lightsOn(x,y,room):
    cnt = 0
    if signal_dict.get((x,y)):
        for nx,ny in signal_dict[(x,y)]:
            if not room[nx][ny]:
                room[nx][ny] = 1 
                cnt += 1 
    return cnt, room 

def isMap(x,y):
    return 0<x<N+1 and 0<y<N+1

def DFS(x,y,room):   
    visit = [[0]*(N+1) for _ in range(N+1)]
    
    q = deque()
    q.append((x,y))
    visit[x][y] = 1 
    cnt = 0
    while q:
        x,y = q.popleft()
        this_cnt,room = lightsOn(x,y,room)
        cnt += this_cnt
        for i in range(4):
            nx,ny = x + dx[i] , y+dy[i]
            if isMap(nx,ny) and room[nx][ny] and not visit[nx][ny]:
                visit[nx][ny] = 1 
                q.append((nx,ny))
    return cnt 

print(DFS(1,1,rooms))
