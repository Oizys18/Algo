# 치즈
import collections
M, N = map(int, input().split())
mat = [[*map(int, input().split())] for _ in range(M)]
cheeseNum = 0

def solve():
    global cheeseNum
    global mat

    def isMap(x, y):
        if 0 <= x <= M-1 and 0 <= y <= N-1:
            return True
        else:
            return False

    def BFS(x, y):
        global mat
        queue = collections.deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            if not visit[x][y]:
                visit[x][y] = 1
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx = x + dx
                    ny = y + dy
                    if isMap(nx, ny):
                        if mat[nx][ny] == 1:
                            mat[nx][ny] = 2
                        elif mat[nx][ny] == 0:
                            queue.append((nx, ny))
    time = 0
    while True:
        visit = [[0]*N for _ in range(M)]
        tempCheese = 0
        # paint cheese
        BFS(0, 0)
        for x in range(M):
            for y in range(N):
                if mat[x][y] == 2:
                    tempCheese += 1
                    mat[x][y] = 0
        if tempCheese == 0:
            return time, cheeseNum
        else:
            cheeseNum = tempCheese
        time += 1

t, c = solve()
print(t)
print(c)
