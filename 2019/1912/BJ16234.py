# 인구이동
from pprint import pprint as pp

N, L, R = map(int, input().split())
mat = [[*map(int, input().split())] for _ in range(N)]
visit = [[0]*N for _ in range(N)]
check = [[0]*N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def isMap(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


def solve(x, y, p):
    queue = []
    queue.append((x, y))
    while queue:
        x, y = queue.pop(0)
        if not visit[x][y]:
            visit[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if isMap(nx, ny):
                    if L <= abs(mat[nx][ny] - mat[x][y]) <= R:
                        check[x][y] = p
                        check[nx][ny] = p
                        queue.append((nx, ny))


rescnt = 0
while True:
    # pp(mat)
    p = 1
    for x in range(N):
        for y in range(N):
            solve(x, y, p)
            p += 1
    visit = [[0]*N for _ in range(N)]

    # 이동할 나라 없음!
    res = 0
    for k in range(N):
        res += sum(check[k])
    if res == 0:
        break

    for x in range(N):
        for y in range(N):
            if check[x][y] and not visit[x][y]:
                visit[x][y] = 1
                countries = []
                cnt = 0
                sump = 0
                paint = check[x][y]
                for i in range(N):
                    for j in range(N):
                        if check[i][j] == paint:
                            cnt += 1
                            sump += mat[i][j]
                            countries.append((i, j))

                for a, b in countries:
                    mat[a][b] = (sump // cnt)

    rescnt += 1
    check = [[0]*N for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
print(rescnt)
