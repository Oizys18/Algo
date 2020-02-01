# 원판돌리기
# 2020.02.01 14:34 ~ 15:39

from pprint import pprint as pp

import collections
N, M, T = map(int, input().split())
mat = [collections.deque([*map(int, input().split())]) for _ in range(N)]
spin_info = [[*map(int, input().split())] for _ in range(T)]

def isMap(x,y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else:
        return False

def check_same(x,y):
    value = mat[x][y]
    flag_a = 0
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1),(0,M-1)]:
        nx = x + dx
        ny = y + dy
        if isMap(nx,ny):
            if mat[nx][ny] == value:
                visit[nx][ny] = 1
                visit[x][y] = 1
                flag_a = 1
    return flag_a

for idx, d, k in spin_info:
    visit = [[0]*M for _ in range(N)]
    for pan in range(1,N+1):
        if (pan) % idx == 0:
            if d == 0:
                mat[pan-1].rotate(k)
            elif d == 1:
                mat[pan-1].rotate(-k)
    flag_b = 0
    for r in range(N):
        for c in range(M):
            if mat[r][c]:
                if check_same(r,c):
                    flag_b = 1
    
    if flag_b:
        for f in range(N):
            for g in range(M):
                if visit[f][g]:
                    mat[f][g] = 0
    
    else:
        sum_pan = 0
        cnt = 0
        average = 0
        for rx in range(N):
            for cy in range(M):
                if mat[rx][cy]:
                    cnt += 1
                    sum_pan += mat[rx][cy]
        if sum_pan == 0:
            continue
        average = sum_pan / cnt
        for xr in range(N):
            for yc in range(M):
                if mat[xr][yc]:
                    if mat[xr][yc] > average:
                        mat[xr][yc] -= 1
                    elif mat[xr][yc] < average:
                        mat[xr][yc] += 1
        
res = 0
for l in range(N):
    for m in range(M):
        if mat[l][m]:
            res += mat[l][m]
print(res)
