# 소가 길을 건너간 이유 6

import sys 
sys.stdin = open('BOJ14466.txt','r')
from pprint import pprint as pp 
from collections import defaultdict,deque
from itertools import combinations

N, K, R = map(int,input().split())
mat = [[0]*(N+1) for _ in range(N+1)]
roads = [tuple(map(int,input().split())) for _ in range(R)]
cows = [tuple(map(int,input().split())) for _ in range(K)]
road_dict = defaultdict(list)
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for road in roads:
    r,c,r2,c2 = road 
    if not road_dict.get((r,c)):
        road_dict[(r,c)] = []
    if not road_dict.get((r2,c2)):
        road_dict[(r2,c2)] = []
    road_dict[(r,c)].append((r2,c2))
    road_dict[(r2,c2)].append((r,c))

def isRoad(x,y,nx,ny):
    return road_dict.get((x,y)) and (nx,ny) in road_dict[(x,y)]
    
def isMap(x,y):
    return 0 < x < N+1 and 0 < y < N+1 


def BFS(start,visit,cnt):
    
    visit[start[0]][start[1]] = cnt 
    check = deque()
    check.appendleft(start)
    while check:
        x,y = check.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if isMap(nx,ny) and not visit[nx][ny] and not isRoad(x,y,nx,ny):
                check.appendleft((nx,ny))
                visit[nx][ny] = cnt
    return visit

visit = [[0]*(N+1) for _ in range(N+1)]
cnt = 1 
for x in range(1,N+1):
    for y in range(1,N+1):
        if not visit[x][y]:
            BFS((x,y),visit,cnt)
            cnt += 1
ansDict = {i:0 for i in range(1,cnt)}

for x,y in cows:
    ansDict[visit[x][y]] += 1

cntMeet = [ansDict[i] for i in ansDict.keys() if ansDict.get(i)]

temp = 0
for a,b in combinations(cntMeet,2):
    temp += a*b
print(temp) 

"""
1. road_dict 생성, 특정 좌표 -> 다음 좌표로 길을 표시 
2. BFS 후 길을 건너지 않고 도달 가능한 곳을 모두 현재의 cnt로 체크 (cluster cnt)
3. 각 소가 어떤 클러스터에 몇마리씩 있는 지 체크 
4. combination을 통해 몇 쌍이 길을 건너야 하는지 계산 
"""