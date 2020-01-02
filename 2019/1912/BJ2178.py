# 미로탐색
# N은 세로 M은 가로 
N, M = map(int, input().split())
maze = [[int(i) for i in input()] for _ in range(N)]
visit = [[0]*M for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
# print(maze)

def pathFinder(x,y):
    if 0 <= x < N and 0 <= y < M:
        if maze[x][y] == 1:
            return True
        else:
            return False
    else: 
        return False

def BFS(depth, x, y):
    queue = []
    queue.append((0, x, y))
    while queue:
        depth, x, y = queue.pop(0)
        if x == N-1 and y == M-1:
            return depth + 1
        if not visit[x][y]:
            visit[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if pathFinder(nx, ny):
                    queue.append((depth+1, nx, ny))


print(BFS(0,0,0))
