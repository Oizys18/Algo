# 핀볼게임
from pprint import pprint as pp 

# 방향 지시등
dr = [0, 1, 2, 3]
# 기본 방향, 좌상우하
direc = [(0, -1), (-1, 0), (0, 1), (1, 0)]

# 좌 상 우 하
# 진입 시 이동 방향
block = {
    1: [(0, -1), (0, 1), (-1, 0), (1, 0)],
    2: [(0, -1), (-1, 0), (1, 0), (0, 1)],
    3: [(1, 0), (-1, 0), (0, 1), (0, -1)],
    4: [(-1, 0), (0, -1), (0, 1), (1, 0)],
    5: [(0, -1), (-1, 0), (0, 1), (1, 0)]
}

# map check


def isMap(x, y):
    if 0 <= x < N+1 and 0 <= y < N+1:
        return True
    else:
        return False


def isWall(x, y):
    if 0 == x or N-1 == x or 0 == y or N-1 == y:
        return True
    else:
        return False


def solve(x, y, startD):
    visit = {}
    start = x, y
    d = startD
    temp = 0

    while True:
        dx, dy = direc[d]
        nx, ny = x + dx, y + dy
        if start == (x, y) and visit.get((x, y)):
            return temp
        if not visit.get((x, y)):
            visit[(x, y)] = [0]*4
            visit[(x, y)][d] = 1
        else:
            if not visit[(x, y)][d]:
                visit[(x, y)][d] = 1
            else:
                temp = 0
                break

        if isMap(nx, ny):
            if mat[nx][ny]:
                # 블랙홀
                if mat[nx][ny] == -1:
                    return temp
                # 블록
                elif 1 <= mat[nx][ny] <= 5:
                    x, y = nx, ny
                    temp += 1
                    if mat[nx][ny] == 1:
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 3
                        elif d == 2:
                            d = 0
                        elif d == 3:
                            d = 2

                    elif mat[nx][ny] == 2:
                        if d == 0:
                            d = 3
                        elif d == 1:
                            d = 2
                        elif d == 2:
                            d = 0
                        elif d == 3:
                            d = 1

                    elif mat[nx][ny] == 3:
                        if d == 0:
                            d = 2
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 1
                    elif mat[nx][ny] == 4:
                        if d == 0:
                            d = 2
                        elif d == 1:
                            d = 3
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 0

                    elif mat[nx][ny] == 5:
                        if d == 0:
                            d = 2
                        elif d == 1:
                            d = 3
                        elif d == 2:
                            d = 0
                        elif d == 3:
                            d = 1

                # 웜홀
                elif 6 <= mat[nx][ny] <= 10:
                    x, y = teleport[(nx, ny)]
            # 그냥 빈 공간
            else:
                x, y = nx, ny

        # 벽을 만남
        else:
            if -1 == nx and d == 1:
                d = 3
            elif N == nx and d == 3:
                d = 1
            elif -1 == ny and d == 0:
                d = 2
            elif N == ny and d == 2:
                d = 0
            temp += 1


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    mat = [[5]*(N+1)]+ [[5] +[*map(int, input().split())] +[5] for _ in range(N)] + [[5]*(N+1)]
    # pp(mat)
    # 진출 방향, 좌상우하

    blackHole = []
    wormHole = dict()
    blocks = dict()
    for x in range(N+1):
        for y in range(N+1):
            if mat[x][y]:
                if mat[x][y] == -1:
                    blackHole.append((x, y))
                elif 1 <= mat[x][y] <= 5:
                    if not blocks.get(mat[x][y]):
                        blocks[mat[x][y]] = []
                    blocks[mat[x][y]].append((x, y))
                elif 6 <= mat[x][y] <= 10:
                    if not wormHole.get(mat[x][y]):
                        wormHole[mat[x][y]] = []
                    wormHole[mat[x][y]].append((x, y))

    teleport = {}
    for k in wormHole:
        teleport[wormHole[k][0]] = wormHole[k][1]
        teleport[wormHole[k][1]] = wormHole[k][0]

    result = 0
    for x in range(N+1):
        for y in range(N+1):
            if not mat[x][y]:
                for startD in range(4):
                    tempRes = solve(x, y, startD)
                    if tempRes:
                        if tempRes >= result:
                            result = tempRes
    print(f"#{testcase} {result}")



"""
1
6
1 1 1 1 1 1 
1 1 -1 1 1 1 
1 -1 0 -1 1 1 
1 1 -1 1 1 1 
1 1 1 1 1 1 
1 1 1 1 1 1
"""
"""
5
10
0 1 0 3 0 0 0 0 7 0 
0 0 0 0 -1 0 5 0 0 0 
0 4 0 0 0 3 0 0 2 2 
1 0 0 0 1 0 0 3 0 0 
0 0 3 0 0 0 0 0 6 0 
3 0 0 0 2 0 0 1 0 0 
0 0 0 0 0 1 0 0 4 0 
0 5 0 4 1 0 7 0 0 5 
0 0 0 0 0 1 0 0 0 0 
2 0 6 0 0 4 0 0 0 4 
6
1 1 1 1 1 1 
1 1 -1 1 1 1 
1 -1 0 -1 1 1 
1 1 -1 1 1 1 
1 1 1 1 1 1 
1 1 1 1 1 1 
8
0 0 0 3 0 0 0 0 
0 0 2 0 0 5 0 0 
0 0 5 0 3 0 0 0 
0 0 1 1 0 0 0 4 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 5 0 
0 0 4 0 0 3 1 0 
2 0 0 4 3 4 0 0 
10
0 4 0 0 0 0 4 0 5 0 
0 0 0 0 0 0 0 0 3 0 
0 0 0 5 6 0 0 0 0 2 
3 0 0 1 0 0 1 4 0 2 
2 0 0 0 0 5 0 0 5 0 
0 0 1 0 2 0 0 0 5 0 
0 0 0 0 0 0 6 1 0 0 
0 0 1 0 2 0 2 4 0 0 
0 0 0 0 0 0 2 0 0 0 
2 0 0 0 0 0 0 3 0 0 
20
0 0 1 0 0 0 0 3 0 3 0 0 0 4 0 0 1 0 4 0 
0 1 2 3 3 0 0 0 0 0 0 0 0 5 0 0 0 0 5 0 
0 0 0 0 0 0 0 0 0 5 0 0 0 5 0 4 0 0 0 0 
4 0 0 0 0 0 0 4 5 0 0 0 3 0 0 0 3 0 0 0 
0 0 0 3 0 4 1 0 3 0 0 0 0 4 0 0 0 2 0 3 
2 2 0 0 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 5 0 5 0 0 0 3 4 
0 0 5 0 -1 5 0 0 5 2 0 0 0 4 2 0 0 3 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 
2 0 0 0 0 3 0 0 3 3 3 0 0 1 0 0 2 0 0 0 
1 5 0 5 0 0 0 0 5 4 5 0 0 0 0 4 2 4 0 0 
0 4 0 0 0 1 3 0 0 0 0 0 1 0 3 0 0 2 0 0 
0 0 0 0 0 0 3 0 1 0 0 1 0 0 0 0 0 3 4 0 
0 4 0 4 0 0 0 0 0 0 0 2 0 0 0 3 0 0 0 2 
0 5 0 0 0 4 1 5 0 0 0 2 0 0 0 0 0 0 0 0 
0 0 0 5 0 0 1 2 0 0 0 3 1 2 5 0 0 0 0 0 
0 4 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 4 0 0 0 0 4 0 0 0 0 0 0 1 4 0 2 0 
0 0 1 0 0 0 0 0 3 0 0 0 0 0 0 0 5 0 0 0 
0 0 0 0 0 0 0 5 0 4 0 0 0 0 0 2 0 0 2 0 

"""
