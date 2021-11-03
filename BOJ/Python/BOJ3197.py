from pprint import pprint as pp
import sys
sys.stdin= open('BOJ3197.txt','r')
from collections import deque
R,C = map(int,sys.stdin.readline().split())

mat = [list(sys.stdin.readline().strip()) for _ in range(R)]
dr = [(0,1),(1,0),(0,-1),(-1,0)]
waterQ, waterTQ = deque(),deque()
swanQ, swanTQ = deque(),deque()
swan = []

water_visit = [[0]*C for _ in range(R)]
swan_visit = [[0]*C for _ in range(R)]
for x in range(R):
    for y in range(C):
        if mat[x][y] == 'L':
            mat[x][y] = '.'
            swan.append((x,y))
            water_visit[x][y] = 1 
            waterQ.append((x,y))
        elif mat[x][y] == '.':
            waterQ.append((x,y))
            water_visit[x][y] = 1 

x1,y1 = swan.pop()
x2,y2 = swan.pop()
swanQ.append((x1,y1))
swan_visit[x1][y1] = 1 

def isMap(x,y):
    return 0 <= x <R and 0 <= y < C

def bfs():
    while swanQ:
        x,y = swanQ.popleft()
        if x==x2 and y == y2:
            return True 
        for i in range(4):
            nx,ny = x+dr[i][0], y+dr[i][1]
            if isMap(nx,ny) and not swan_visit[nx][ny]: 
                if mat[nx][ny] == '.':
                    swanQ.append((nx,ny))
                else:
                    swanTQ.append((nx,ny))  
                swan_visit[nx][ny] = 1 
    return False 
    
def melt():
    while waterQ:
        x,y = waterQ.popleft()
        mat[x][y] = '.'
        for i in range(4):
            nx,ny = x+dr[i][0], y+dr[i][1]
            if isMap(nx,ny) and not water_visit[nx][ny] and mat[nx][ny] == 'X':
                waterTQ.append((nx,ny))
                water_visit[nx][ny] = 1
time = 0 
while True:
    melt()
    if bfs():
        print(time)
        break 
    waterQ,swanQ = waterTQ, swanTQ
    waterTQ, swanTQ = deque(), deque() 
    time += 1 

""" 
1. 백조 위치 특정 
2. 물의 위치 저장 -> waterQ -> dr 확인하면서 주변에 얼음 있으면 iceQ에 넣기  
3. 얼음 위치 저장 -> iceQ -> pop한 좌표를 녹이기, 주변에 얼음 있으면 iceTQ

물(백조)의 움직임 bfs와 녹는 얼음의 움직임 bfs를 각각 현재,임시의 4개의 큐를 사용해 풀어야한다. 

*그냥 bfs 후 이진탐색으로 time을 찾는 방법도 있는 것 같은데, 이 방법이 더 좋은 풀이 같아서 이 방법으로 풀었다. 
"""            



# def isAdjacent(x,y):
#     for i in range(4):
#         nx,ny = x+dr[i][0], y+dr[i][1]
#         if isMap(nx,ny) and mat[nx][ny] != 'X':
#             return True
#     else:
#         return False

# for x in range(R):
#     for y in range(C):
#         if mat[x][y] == 'L':
#             swan.append((x,y))
#         elif mat[x][y] == 'X':
#             ice.add((x,y))
#             if  isAdjacent(x,y):
#                 nxt_melt.add((x,y))

# time = 0
# flag = 0 
# visit = [[0]*C for _ in range(R)]
# temp_melt = set()
# while not flag:
#     q = deque()
#     if not temp_melt:
#         visit[swan[0][0]][swan[0][1]] = 1 
#         q.append((swan[0]))
#     else:
#         for x,y in temp_melt:
#             visit[x][y] = 1 
#             q.append((x,y))

#     while q: 
#         x,y = q.popleft()
#         print(x,y,q)
#         for i in range(4):
#             nx, ny = x + dr[i][0], y + dr[i][1] 
#             if ice and (nx,ny) in ice: 
#                 continue
#             if isMap(nx,ny) and not visit[nx][ny] :
#                 visit[nx][ny] = 1 
#                 if (nx,ny) == swan[1]:
#                     flag = 1 
#                     break 
#                 q.append((nx,ny))

#     if flag: 
#         print(time)
#         break  
#     temp_melt = set()
#     for x,y in ice:
#         for i in range(4):
#             nx,ny = dr[i][0]+x, dr[i][1]+y
#             if isMap(nx,ny) and (nx,ny) in nxt_melt:
#                 temp_melt.add((x,y))
#     ice = ice.difference(nxt_melt)
#     nxt_melt = temp_melt
#     time += 1 































"""
이것도 시간초과 
"""
# swan = []
# ice = set()

# def isMap(x,y):
#     return 0 <= x <R and 0 <= y < C

# def isAdjacent(x,y):
#     for i in range(4):
#         nx,ny = x+dr[i][0], y+dr[i][1]
#         if isMap(nx,ny) and mat[nx][ny] != 'X':
#             return True
#     else:
#         return False

# for x in range(R):
#     for y in range(C):
#         if mat[x][y] == 'X' and isAdjacent(x,y):
#             ice.add((x,y))
#         elif mat[x][y] == 'L':
#             swan.append((x,y))

# melt_date = [[0]*C for _ in range(R)]
# def melts(ice):
#     visit = [[0]*C for _ in range(R)]
#     q = deque()
#     for x,y in ice:
#         visit[x][y] = 1 
#         q.append((x,y,1))
#         melt_date[x][y] = 1 
#     while q:
#         x,y,depth = q.popleft()
#         for i in range(4):
#             nx,ny = x+dr[i][0],y+dr[i][1]
#             if isMap(nx,ny) and not visit[nx][ny] and mat[nx][ny] == 'X':
#                 visit[nx][ny] = 1 
#                 melt_date[nx][ny] = depth + 1 
#                 q.append((nx,ny,depth+1))
# melts(ice)

# def bfs(x,y):
#     q = deque()
#     q.append((x,y,0))
#     visit =[[0]*C for _ in range(R)]
#     check =[[0]*C for _ in range(R)]
#     visit[x][y] = 1 
#     while q:
#         x,y,time = q.popleft()
#         for i in range(4):
#             nx,ny = x+dr[i][0], y +dr[i][1]
#             if isMap(nx,ny):
#                 if not visit[nx][ny]:
#                     visit[nx][ny] = 1
#                     arrival = max(time,melt_date[nx][ny])
#                     check[nx][ny] = arrival
#                     q.append((nx,ny,arrival))
#                 elif check[nx][ny] > time:

#                     if melt_date[nx][ny] > time:
#                         q.append((nx,ny,melt_date[nx][ny]))
#                     q.append((nx,ny))
#                     if mat[nx][ny] == 'L':
#                         return True







"""
# 얼음 set -> visit 체크 + depth 체크 
# swan bfs -> 전부 검사 중, 만약 depth 값이 있는 (n일에 녹는 얼음) 발견 시 배낭에 day 추가 
# 다음 swan에 도달했을 때 최솟값 뱉기 


첫번째 백조 닿아있는 모든 물에 1 
두번째 백조 닿아있는 모든 물에 2

"""
# 시간초과
# from collections import deque
# R,C = map(int,sys.stdin.readline().split())
# mat = [[0 if i=='.' else 1 if i=='X' else 2 for i in sys.stdin.readline().strip() ] for _ in range(R)]
# dr = [(0,1),(0,-1),(-1,0),(1,0)]

# def isMap(x,y):
#     return 0 <= x <R and 0 <= y < C


# ice = set()
# swan = []
# for x in range(R):
#     for y in range(C):
#         if mat[x][y] == 1:
#             ice.add((x,y))
#         elif mat[x][y] ==2:
#             swan.append((x,y))

# def travel(x,y):
#     q = deque()
#     visit = [[0]*C for _ in range(R)]
#     q.append((x,y))
#     visit[x][y] = 1
#     while q:
#         x,y = q.popleft()
#         for i in range(4):
#             nx,ny = x+dr[i][0], y+dr[i][1]
#             if isMap(nx,ny) and not visit[nx][ny] and isAdjacent(nx,ny):
#                 if mat[nx][ny] == 2:
#                     return True
#                 visit[nx][ny] = 1 
#                 q.append((nx,ny))
#     return False 

# time = 1
# while ice:
#     if travel(swan[0][0],swan[0][1]):
#         print(time)
#         break 
#     will_melt = set()
#     for x,y in ice:
#         if isAdjacent(x,y):
#             will_melt.add((x,y))
#     for x,y in will_melt:
#         mat[x][y] = 0
#         ice.remove((x,y))
#     time += 1 
