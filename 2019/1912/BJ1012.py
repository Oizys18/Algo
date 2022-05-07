# 유기농 배추

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def isMap(x, y):
    if 0 <= x <= N-1 and 0 <= y <= M-1:
        if mat[x][y] == 1:
            return True
        else:
            return False
    else:
        return False


def BFS(x, y):
    queue = []
    queue.append((x, y))
    while queue:
        x, y = queue.pop(0)
        if mat[x][y]:
            mat[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if isMap(nx, ny):
                    queue.append((nx, ny))


for T in range(int(input())):
    M, N, K = map(int, input().split())
    mat = [[0]*M for _ in range(N)]
    bcDic = {}
    for k in range(K):
        x, y = map(int, input().split())
        bcDic[k] = (y, x)
        mat[y][x] = 1

    res = 0
    for ay, ax in bcDic.values():
        if mat[ay][ax]:
            BFS(ay, ax)
            res += 1
    print(res)
