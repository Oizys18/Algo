# 새로운 게임
import sys
sys.stdin = open('BOJ17780.txt','r')
from pprint import pprint as pp 


# 다음 칸 정보 확인 
def check_next (nx,ny):
    return 0 <= nx < N and 0 <= ny <N and info_mat[nx][ny]!=2

#방향전환
def change_direction(direction):
    if direction%2:return direction+1
    return direction-1

# 방향, →, ←, ↑, ↓
mv = {
    1: (0,1),
    2: (0,-1),
    3: (-1,0),
    4: (1,0)
}

N,K = map(int,input().split())
info_mat = [list(map(int,input().split())) for _ in range(N)]
mat = [[[] for _ in range(N)] for _ in range(N)]
data = []

for k in range(K):
    x,y,direction = map(int,input().split())
    mat[x-1][y-1].append(k)
    data.append([k,x-1,y-1,direction])

def solve():
    for turn in range(1000):
        for k,x,y,d in data:
            if mat[x][y][0] != k: continue
            nx, ny = x+mv[d][0], y+mv[d][1]

            if not check_next(nx,ny):
                # blue || out of range : 방향전환
                d = change_direction(d)
                data[k][3] = d
                nx, ny = x+mv[d][0], y+mv[d][1] 

                if not check_next(nx,ny):
                    continue
            if info_mat[nx][ny]==1:
                mat[x][y].reverse()

            mat[nx][ny] += mat[x][y]
            mat[x][y] = [] 

            for nk in mat[nx][ny]:
                data[nk][1] = nx
                data[nk][2] = ny
            if len(mat[nx][ny])>=4:
                return turn +1
    return -1

print(solve())

