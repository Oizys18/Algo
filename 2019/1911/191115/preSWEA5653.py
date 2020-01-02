import sys
sys.stdin = open('5653.txt','r')
from pprint import pprint as pp

testcase = int(input())
tc = 1

def isMap(x, y):
    if 0 <= x < N and 0 <= y < M:
        if mat[x][y]:
            return True
    else:
        return False

def wide(mat):
    # for j in range(n):
    for i in range(len(mat)):
        mat[i] = [0] + mat[i] + [0]
        Mlen = len(mat[i])
    mat.insert(0,[0]*(Mlen))
    mat.append([0]*(Mlen))
        

def virus(K):
    queue = []
    time = 1
    for x in range(M):
        for y in range(N):
            if mat[x][y]:
                queue.append((x,y))
    while queue:
        x, y = queue.pop(0)
        if mat[x][y]:
            # 조건문 수정 필요
            if mat[x][y] > time:
                continue
            elif mat[x][y] == time:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if isMap(nx,ny):
                        if mat[x][y] >= mat[nx][ny]:
                            # 테두리 1줄 늘리기 
                            wide(mat)
                            # 더하는 것 수정 필요 
                            mat[nx][ny] = time + mat[x][y]
        else:
            continue
        mat[x][y] -= 1
        time += 1
        if time == K:
            break
    alive = 0
    for x in range(len(mat[0])):
        for y in range(len(mat)):
            if mat[x][y]:
                alive += 1
    print(mat)
    return alive

                
for T in range(tc):
    N, M, K = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    check = [[0]*M for _ in range(N)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    print(virus(1))

# 1. check 행렬에 얼려둔걸 가져오기..?
# 2. 자동으로 시간이 되면 녹게 만들기..?