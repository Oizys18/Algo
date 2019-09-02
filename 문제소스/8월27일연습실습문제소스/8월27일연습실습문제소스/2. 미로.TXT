import sys
sys.stdin = open("input.txt", "r")

def check(x, y):
    if x < 0 or x > N-1 : return False
    if y < 0 or y > N-1 : return False
    if maze[x][y] == 1  : return False
    return True


def DFS(x, y):
    stack = [0] * (N*N)
    top = -1

    top += 1 ; stack[top] = x, y

    while top != -1:
        x, y = stack[top] ; top -= 1

        if maze[x][y] == 3 : return 1
        if maze[x][y] != 1 :
            maze[x][y] = 1
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                if check(newX, newY) :
                    top += 1 ; stack[top] = newX, newY
    return 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2 :
                sX = i
                sY = j

    print('#%d'%tc, DFS(sX, sY))




import sys
# sys.stdin = open("input.txt", "r")
# 
# def DFSr(x, y):
#     global found
#     if not 0 <= x < N or not 0 <= y < N or found or maze[x][y] == 1 : return
#     if maze[x][y] == 3 : found = 1; return
# 
#     maze[x][y] = 1
#     DFSr(x, y+1)
#     DFSr(x, y-1)
#     DFSr(x+1, y)
#     DFSr(x-1, y)
# 
# 
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     maze = [[int(x) for x in input()] for _ in range(N)]
# 
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2 :
#                 sX = i
#                 sY = j
# 
#     found = 0
#     DFSr(sX, sY)
#     print('#%d'%tc, found)