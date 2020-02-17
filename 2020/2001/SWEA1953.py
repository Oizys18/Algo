# 탈주범 검거
pipeDic = {
    1: [(0, 1), (0, -1), (-1, 0), (1, 0)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(0, 1), (1, 0)],
    6: [(0, -1), (1, 0)],
    7: [(0, -1), (-1, 0)],
}


def isMap(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else:
        return False

def isPath(x,y,nx,ny):
    nxt = mat[nx][ny]
    if y < ny and nxt in [1,3,6,7]:
        return True
    elif y > ny and nxt in [1,3,4,5]:
        return True
    if x > nx and nxt in [1,2,5,6]:
        return True
    elif x < nx and nxt in [1,2,4,7]:
        return True
    return False
    

def BFS(x, y):
    queue = []
    queue.append((1, x, y))
    cnt = 0
    while queue:
        depth, x, y = queue.pop(0)
        if depth > L:
            continue
        if not visit[x][y]:
            visit[x][y] = 1
            cnt += 1
            for dx, dy in pipeDic[mat[x][y]]:
                nx = x + dx
                ny = y + dy
                if isMap(nx, ny):
                    if isPath(x,y,nx,ny) and not visit[nx][ny]:
                        queue.append((depth+1,nx,ny))
    return cnt

T = int(input())
for testcase in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    mat = [[*map(int, input().split())] for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    print(f"#{testcase} {BFS(R, C)}")
