import sys
sys.stdin = open('1953.txt','r')
from pprint import pprint as pp


def isMap(x, y, nx, ny):
    if 0 <= nx < N and 0 <= ny < M:
        if mat[nx][ny]:
            # print('new pipe')
            if y < ny:
                if mat[nx][ny] in [1,3,6,7]:
                    return True
            elif y > ny:
                if mat[nx][ny] in [1,3,4,5]:
                    return True
            if x > nx:
                if mat[nx][ny] in [1,2,5,6]:
                    return True
            elif x < nx:
                if mat[nx][ny] in [1,2,4,7]:
                    return True
            return False
        return False
    return False
    
def BFS(x,y):
    queue = []
    direction = 0
    queue.append((1,x,y))
    cnt = 0
    while queue:
        depth, x, y = queue.pop(0)
        if not visit[x][y]:
            visit[x][y] = 1
            cnt += 1
            for i in pipeDic[mat[x][y]]:
                dx, dy = i
                nx = x + dx
                ny = y + dy
                if isMap(x,y,nx,ny):
                    if depth+1 > L:
                        continue
                    queue.append((depth+1,nx,ny))
    return cnt
# up:(-1,0) # down: (1,0) # left: (0,-1) # right: (0,1)
pipeDic = {
    1:[(0,1),(0,-1),(-1,0),(1,0)],
    2:[(-1,0),(1,0)],
    3:[(0,-1),(0,1)],
    4:[(-1,0),(0,1)],
    5:[(0,1),(1,0)],
    6:[(0,-1),(1,0)],
    7:[(0,-1),(-1,0)],
}

# left = 1, up = 2, right = 3, down = 4

for T in range(int(input())):
    N, M, R, C, L = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    print(f"#{T+1} {BFS(R,C)}")

    