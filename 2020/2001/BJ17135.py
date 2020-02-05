# 캐슬 디펜스
from pprint import pprint as pp

import collections
import itertools
import copy
N, M, D = map(int, input().split())
mat = [[*map(int, input().split())] for _ in range(N)] + [[0]*M]
archers = [0]*M

def isMap(x, y):
    if 0 <= x < N + 2 and 0 <= y < M:
        return True
    else:
        return False
def BFS(field, x, y):
    visit = [[0]*M for _ in range(N+1)]
    queue = []
    queue.append((0, x, y))
    while queue:
        depth, x, y = queue.pop(0)
        if depth > D:
            pp(visit)
            continue
        if not visit[x][y]:
            visit[x][y] = 1
            if field[x][y] == 1:
                pp(visit)
                return (x,y)
            for dx, dy in [(0, -1),(-1, 0),(0, 1)]:
                nx = x + dx
                ny = y + dy
                if isMap(nx, ny):
                    queue.append((depth+1, nx, ny))    

def fight():
    kills = 0
    field = collections.deque(copy.deepcopy(mat))
    pp(field)
    while True:
        turnKill = set()
        for x in range(N + 1):
            for y in range(M):
                if field[x][y] == 2:
                    print(x,y)
                    killed = BFS(field, x, y)
                    if killed:
                        kills += 1
                        turnKill.add(killed)
        for xt,yt in turnKill:
            field[xt][yt] = 0
        field.extendleft([[0]*M])
        del field[N]

        flag = 0
        for a in range(N):
            for b in range(M):
                if field[a][b]:
                    flag = 1
        if not flag:
            print(kills)
            return kills

res = 0
for chosen_archer in itertools.combinations(range(M), 3):
    for ca in chosen_archer:
        mat[N][ca] = 2
    tactics = fight()
    if res < tactics:
        res = tactics
    mat[N] = [0]*M

print(res)
