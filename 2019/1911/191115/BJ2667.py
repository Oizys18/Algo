N = int(input())
mat = [input() for _ in range(N)]
visit = [[0]*N for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def isMap(x, y, nx, ny):
    if 0 <= nx < N and 0 <= ny < N:
        if int(mat[nx][ny]):
            return True
        else:
            return False
    else:
        return False

def BFS(x, y, cnt):
    queue = []
    queue.append((x,y))
    while queue:
        x, y = queue.pop(0)
        if not visit[x][y]:
            visit[x][y] = cnt
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if isMap(x, y, nx, ny):
                    queue.append((nx,ny))
    
cnt = 1
for x in range(N):
    for y in range(N):
        if int(mat[x][y]) and not visit[x][y]:
            # print(visit)
            # print(mat[x][y])
            BFS(x, y, cnt)
            cnt += 1
temp = [0]*cnt
for i in range(N):
    for j in range(N):
        if visit[i][j]:
            temp[visit[i][j]] += 1

print(len(temp)-1)
# print(temp)
for k in sorted(temp[1:]):
    print(k)