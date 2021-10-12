import sys 
sys.stdin = open('BOJ7569.txt','r')
from pprint import pprint as pp 
"""
처음 내가 푼 것. deque 넣으니까 풀리긴 했는데 3000ms 정도 걸림 
"""
from collections import deque
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

# x,y,z (n,m,h)
dr = [(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]

def bfs(riped_tomato):
    q = deque((0,x,y,z) for x,y,z in riped_tomato)
    visit = [[[0]*H for _ in range(M)] for _ in range(N)]
    mx_depth = 0
    ripen = set()
    while q:
        depth,x,y,z = q.popleft()
        mx_depth = max(depth,mx_depth)
        for dx,dy,dz in dr:
            nx,ny,nz = x+dx,y+dy,z+dz
            if isMap(nx,ny,nz) and not visit[nx][ny][nz]:
                visit[nx][ny][nz] = 1 
                q.append((depth+1,nx,ny,nz))
                ripen.add((nx,ny,nz))
    return mx_depth,ripen

mxD, ripen = bfs(riped_tomato)
unripe_tomato.difference_update(ripen)

if unripe_tomato:
    print(-1)
else:
    print(mxD)



"""
1등 코드 참고해서 수정함 
"""
from collections import deque
M,N,H = map(int,input().split())
box = [[[0]*M for _ in range(N)] for _ in range(H) ]
dr = [(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]
q = deque()
ripe = 0 
num = 0
for h in range(H):
    box[h] = [[*map(int,input().split())] for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                q.append((h,n,m))
                ripe += 1
                num += 1 
            elif box[h][n][m] == -1:
                ripe += 1
def isRaw(h,n,m):
    return 0 <= h < H and 0 <= n < N and 0 <= m < M and box[h][n][m] == 0

cnt = 0 
while q:
    h,n,m = q.popleft()
    num -= 1
    for dh,dn,dm in dr:
        nh,nn,nm = h+dh,n+dn,m+dm
        if isRaw(nh,nn,nm):
            box[nh][nn][nm] = 1
            ripe += 1 
            q.append((nh,nn,nm))
    if num == 0:
        cnt += 1 
        num = len(q)

print(cnt-1 if ripe == H*M*N else -1)