# # 로봇 청소기, 재도전!
from pprint import pprint as pp
N, M = map(int, input().split())
r, c, d = map(int, input().split())
mat = [[*map(int, input().split())] for _ in range(N)]
visit = [[0]*M for _ in range(N)]
#     북        동      남      서
dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
res = 0


def isPath(x, y):
    if 0 <= x < N and 0 <= y < M:
        if mat[x][y] != 1:
            return True
        else:
            return False
    else:
        return False


def solve(x, y, d):
    global res
    # 1번
    visit[x][y] = 1
    res += 1
    temp = 0
    # 2번
    while True:
        # 2-a
        dx, dy = dr[d-1]
        nx, ny = x + dx, y + dy

        if isPath(nx, ny):
            if visit[nx][ny] == 0:
                d = (d-1) % 4
                visit[nx][ny] = 1
                x = nx
                y = ny
                temp = 0
                res += 1
                continue
            
        if temp == 4:
            dx, dy = dr[d-2]
            nx, ny = x + dx, y + dy
            if isPath(nx, ny):
                temp = 0
                x = nx
                y = ny
                continue
            else:
                return res
        d = (d-1) % 4
        temp += 1

print(solve(r,c,d))
# d = int(input())
# dr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# print(dr[d-1])
# print((d-1)%4)
"""
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

4 4
0 0 0 
0 0 1 0
1 0 0 0
1 0 1 1
0 0 0 0
"""