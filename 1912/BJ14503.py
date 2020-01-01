# 로봇청소기
from pprint import pprint as pp

N, M = map(int, input().split())
r, c, d = map(int, input().split())
mat = [[*map(int, input().split())] for _ in range(N)]
visit = [[0]*M for _ in range(N)]
check = [0]*4
# 0: 북, 1:동, 2:남, 3:서
# dr = [0, 1, 2, 3]
drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0


def isMap(x, y):
    if 0 <= x < N and 0 <= y < M:
        if mat[x][y] == 0:
            return True
        else:
            return False
    else:
        return False


def isWall(x, y):
    if 0 <= x < N and 0 <= y < M:
        if mat[x][y] == 1:
            return True
        else:
            return False
    else:
        return False


res = 0


def solve(x, y, d):
    global check
    global res
    while True:
        if not visit[x][y]:
            visit[x][y] = 1
            res += 1
        # 좌측
        dx, dy = drc[d-1]
        nx = x + dx
        ny = y + dy

        if sum(check) == 4:
            dx, dy = drc[d-2]
            nx = x + dx
            ny = y + dy
            if isWall(nx, ny):
                return res
            else:
                if isMap(nx, ny):
                    x = nx
                    y = ny
                    check = [0]*4
        else:
            if isMap(nx, ny):
                d = (d-1) % 4
                x = nx
                y = ny
                check = [0]*4

            else:
                check[d-1] = 1
                d = (d-1) % 4

print(solve(r, c, d))

