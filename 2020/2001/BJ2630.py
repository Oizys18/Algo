from pprint import pprint as pp
N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]
visit = [[0]*N for _ in range(N)]
paint = 1
paint2 = -1


def solve(x, y):
    global paint
    if not visit[x][y]:
        idx = 0
        for i in range(N-y):
            if not visit[x][y+i]:
                if mat[x][y+i]:
                    idx = i
                else:
                    break
        for a in range(idx+1):
            for b in range(idx+1):
                visit[x+a][y+b] = paint
        paint += 1
        # pp(visit)


def solve2(x, y):
    global paint2
    if not visit[x][y]:
        idx = 0
        for i in range(N-y):
            if not visit[x][y+i]:
                if mat[x][y+i] == 0:
                    idx = i
                else:
                    break
        for a in range(idx+1):
            for b in range(idx+1):
                visit[x+a][y+b] = paint2
        paint2 -= 1
        pp(visit)


for x in range(N):
    for y in range(N):
        if mat[x][y] == 1:
            solve(x, y)
        else:
            solve2(x, y)
print(visit)
