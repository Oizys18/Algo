from pprint import pprint as pp

# 빙산 retry
N, M = map(int, input().split())
mat = [[*map(int, input().split())] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solve():
    def isMap(x,y):
        if 0 <= x < N and 0 <= y < M:
            return True
        else:
            return False

    def BFS(x,y):
        queue = []
        queue.append((x,y))
        while queue:
            x,y = queue.pop(0)
            if not visit[x][y]:
                visit[x][y] = 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if isMap(nx,ny):
                        if mat[nx][ny]:
                            queue.append((nx,ny))

    def checkMelt(x,y):
        melt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isMap(nx,ny):
                if mat[nx][ny] == 0:
                    melt += 1
        return melt

    time = 0
    while True:
        meltDic = {}
        visit = [[0]*M for _ in range(N)]
        iceCNT = 0
        # 빙산 갯수 세기 
        for x in range(N):
            for y in range(M):
                if mat[x][y]:  
                    meltDic[(x,y)] = checkMelt(x,y)
                    if not visit[x][y]:
                        BFS(x,y)
                        iceCNT += 1

        # 빙산이 2개 이상 : 시간 리턴
        if iceCNT > 1:
            return time
        # 빙산 0개 : 다 녹아벌임; 0 출력 
        elif iceCNT == 0:
            return 0
    

        # 빙산 녹이기
        for k,v in meltDic.items():
            x, y = k
            melt = v
            if mat[x][y] <= melt:
                mat[x][y] = 0
            elif mat[x][y] > melt:
                mat[x][y] -= melt

        # 시간 += 1
        time += 1

print(solve())





































"""
def isMap(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else:
        return False

# 함수 
def solve():
    time = 0
    # 반복 ( while ) 
    while True:
        checkSpeed = [[0]*M for _ in range(N)]
        visit = [[0]*M for _ in range(N)]
        
        # 녹이기
        for x in range(N):
            for y in range(M):
                temp = 0 
                if mat[x][y]:
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if isMap(nx,ny):
                            if mat[nx][ny] == 0:
                                temp += 1
                checkSpeed[x][y] = temp
        for x in range(N):
            for y in range(M):
                if mat[x][y]:
                    if mat[x][y] <= checkSpeed[x][y]:
                        mat[x][y] = 0
                    else:
                        mat[x][y] -= checkSpeed[x][y]


        # time 증가  
        time += 1
        # 빙산 덩어리 갯수 세기 (BFS)
        mass = 0
        for x in range(N):
            for y in range(M):
                if mat[x][y] and not visit[x][y]:
                    mass += 1
                    queue = []
                    queue.append((x,y))
                    while queue:
                        x,y = queue.pop(0)
                        if not visit[x][y]:
                            visit[x][y] = 1
                            for i in range(4):
                                nx = x + dx[i]
                                ny = y + dy[i]
                                if isMap(nx,ny):
                                    if mat[nx][ny]:
                                        queue.append((nx,ny))
        # 2개 이상이면 return time 
        # 0이면 return 0 
        if mass > 1:
            return time
        elif mass == 0:
            return 0
        
print(solve())
"""

"""
5 7
0 0 0 0 0 0 0
0 2 2 2 2 2 0
0 2 5 0 5 2 0
0 2 2 2 2 2 0
0 0 0 0 0 0 0

"""