# Turn on Fire 
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ11967.txt', 'r')

from collections import deque

N,M = map(int,input().split())
signals = [[*map(int,input().split())] for _ in range(M)]
lighted = set()
lighted.add((1,1))
dx = [0,0,-1,1]
dy = [-1,1,0,0]

signal_dict = dict()
for x,y,a,b in signals:
    if not signal_dict.get((x,y)):
        signal_dict[(x,y)] = []
    signal_dict[(x,y)].append((a,b))


def lightsOn(x,y):
    if signal_dict.get((x,y)):
        for nx,ny in signal_dict[(x,y)]:
            lighted.add((nx,ny))
    return 

def isMap(x,y):
    return 0<x<N+1 and 0<y<N+1

def DFS(x,y):   
    visit = [[0]*(N+1) for _ in range(N+1)]
    visit[x][y] = 1 
    q = deque()
    q.append((x,y))
    cnt = 0 
    while q:
        x,y = q.popleft()
        lightsOn(x,y)
        for i in range(4):
            nx,ny = x + dx[i] , y+dy[i]
            if isMap(nx,ny) and (nx,ny) in lighted and not visit[nx][ny]:
                visit[nx][ny] = 1 
                q.append((nx,ny))
    return  

while True:
    this = len(lighted)
    DFS(1,1)
    if this == len(lighted):
        break 

print(len(lighted))

