# SWEA5105 미로의 거리 
"""
NxN 미로 -> 출발지와 목적지 부여 
최소 몇칸을 지나야 출발지에서 도착지에 다다를 수 있는지 알아내기 

경로 O : 지나야하는 최소 칸의 수 
경로 X : 0 출력

1. 행렬로 지도 받기 
2. isPath 함수 : 사방 검색 후 
    Path 면 (0)이면 True 
    1이거나 범위 밖이면 False
3. BFS(depth,start,end):
    queue 를 사용 
    while : 
        하나씩 들어가보고 visit에 없으면 (depth,좌표)를 추가
        길을 찾아서 있으면 그 좌표를 queue에 (depth+1,좌표)로 추가 
        visit에 end의 좌표가 있으면(end에 도착했을 때) : 탐색 종료 
>> depth 를 출력 
    
"""
import sys
sys.stdin = open('input3.txt','r')

def isPath(r,c):
    if (r <= N-1 and r >= 0) and (c <= N-1 and c >= 0):
        # print('1')
        if mat[r][c] == '0' or mat[r][c] == '3':
            return True
        else:
            return False
    else:
        return False

def BFS(depth,start,end):
    queue = []
    visit = []
    queue.append((depth,start))
    while queue:
        depth,node = queue.pop(0)
        x = node[0]
        y = node[1] 
        if node not in visit:
            visit.append(node)
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                # print(newX,newY)
                if (newX,newY) == end:
                    return depth
                if isPath(newX,newY):
                    node = (newX,newY)
                    queue.append((depth+1,node))
    return 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]
for T in range(int(input())):
    N = int(input())
    mat = []
    for _ in range(N):
        mat.append(input())
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == '2':
                start = (r,c)
            if mat[r][c] == '3':
                end = (r,c)
    print("#{0} {1}".format(T+1,BFS(0,start,end)))

    

