import sys 
sys.stdin = open('BOJ7569.txt','r')
from pprint import pprint as pp 

from copy import deepcopy as dc 
M,N,H = map(int,input().split())
box = [[[0]*H for _ in range(M)] for _ in range(N) ]
unripe_tomato = set()
riped_tomato = set()
for h in range(H):
    for n in range(N):
        for i,m in enumerate(map(int,input().split())):
            box[n][i][h] = m
            if m == 0:
                unripe_tomato.add((n,i,h))
            if m == 1:
                riped_tomato.add((n,i,h))
                
def isMap(x,y,z):
    return 0 <= x < N and 0 <= y < M and 0 <= z < H and box[x][y][z] == 0

def isRipe(box):
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[n][m][h] == 0:
                    return False
    else:
        return True 

# x,y,z (n,m,h)
dr = [(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]
visit = [[[0]*H for _ in range(M)] for _ in range(N) ]

def bfs(riped_tomato):
    q = [(0,x,y,z) for x,y,z in riped_tomato]
    visit = [[[0]*H for _ in range(M)] for _ in range(N)]
    mx_depth = 0
    ripen = set()
    while q:
        depth,x,y,z = q.pop(0)
        mx_depth = max(depth,mx_depth)
        for dx,dy,dz in dr:
            nx,ny,nz = x+dx,y+dy,z+dz
            if isMap(nx,ny,nz) and not visit[nx][ny][nz] :
                visit[nx][ny][nz] = depth+1 
                q.append((depth+1,nx,ny,nz))
                ripen.add((nx,ny,nz))
    return mx_depth,ripen
mxD, ripen = bfs(riped_tomato)


# def ripe(riped):
#     ripen = set()
#     for x,y,z in riped:
#         for dx,dy,dz in dr:
#             nx,ny,nz = x+dx,y+dy,z+dz
#             if isMap(nx,ny,nz) and (nx,ny,nz) not in ripen:
#                 ripen.add((nx,ny,nz))
#     return ripen


# time = 0
# while True:
#     if isRipe(box):
#         print(time)
#         break
#     time += 1 
#     pre_box = dc(box)
#     riped = set()
#     for h in range(H):
#         for n in range(N):
#             for m in range(M):
#                 if box[n][m][h] == 1:
#                     riped.add((n,m,h))
#     ripen = ripe(riped)
#     for x,y,z in ripen:
#         box[x][y][z] = 1 
#     if box == pre_box:
#         print(-1)
#         break