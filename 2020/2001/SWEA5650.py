# 핀볼게임

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
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


def isWall(x, y):
    if 0 == x or N-1 == x or 0 == y or N-1 == y:
        return True
    else:
        return False

# x,y,방향


def solve(x, y, startD):
    visit = [[[-1]]*N for _ in range(N)]
    start = x, y
    # start direction (current)
    d = startD
    temp = 0
    while True:
        dx, dy = direc[d]
        nx, ny = x + dx, y + dy
        
        if d not in visit[x][y]:
            visit[x][y].append(d)
        else:
            if (x, y) == start:
                return temp
            if d in visit[x][y]:
                break
        if isMap(nx, ny):

            # else:
            # 다음 블록에 뭔가 있음
            if mat[nx][ny]:
                # 블랙홀
                if mat[nx][ny] == -1:
                    return temp
                # 블록
                elif 1 <= mat[x][y] <= 5:
                    dx, dy = block[d]
                    x, y = nx + dx, ny + dy
                    temp += 1
                    if mat[x][y] == 1:
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 3
                        elif d == 2:
                            d = 0
                        elif d == 3:
                            d = 2

                    elif mat[x][y] == 2:
                        if d == 0:
                            d = 3
                        elif d == 1:
                            d = 2
                        elif d == 2:
                            d = 0
                        elif d == 3:
                            d = 1

                    elif mat[x][y] == 3:
                        if d == 0:
                            d = 2
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 1
                    elif mat[x][y] == 4:
                        if d == 0:
                            d = 2
                        elif d == 1:
                            d = 3
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 0

                    elif mat[x][y] == 5:
                        if d == 0:
                            d = 2
                        elif d == 1:
                            d = 3
                        elif d == 2:
                            d = 0
                        elif d == 3:
                            d = 1

                # 웜홀
                elif 6 <= mat[x][y] <= 10:
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
    mat = [[*map(int, input().split())] for _ in range(N)]
    # 진출 방향, 좌상우하

    blackHole = []
    wormHole = dict()
    blocks = dict()
    for x in range(N):
        for y in range(N):
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

    result = 0
    for x in range(N):
        for y in range(N):
            if not mat[x][y]:
                for startD in range(4):
                    tempRes = solve(x, y, startD)
                    if tempRes:
                        if tempRes >= result:
                            result = tempRes
print(result)

"""
1
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
"""
