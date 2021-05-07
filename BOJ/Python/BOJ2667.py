# 단지번호
from pprint import pprint as pp

import collections
N = int(input())
mat = [input() for _ in range(N)]
visit = [[0]*N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dan = 1


def isDanji(x, y):
    if 0 <= x < N and 0 <= y < N:
        if mat[x][y] == '1':
            return True
        else:
            return False
    else:
        return False


def BFS(x, y):
    global dan
    queue = collections.deque()
    queue.append((x, y))
    cnt = 0
    dan += 1
    while queue:
        x, y = queue.popleft()
        if not visit[x][y]:
            visit[x][y] = dan
            cnt += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if isDanji(nx, ny):
                    queue.append((nx, ny))
    return cnt


danDic = {}
for x in range(N):
    for y in range(N):
        if mat[x][y] == '1' and not visit[x][y]:
            danDic[dan] = BFS(x, y)


print(dan-1)
for i in sorted(danDic.values()):
    print(i)
