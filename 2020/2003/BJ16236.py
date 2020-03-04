# 아기상어

"""
아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 
나머지 칸은 모두 지나갈 수 있다. 
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
따라서, 크기가 같은 물고기는 먹을 수 없지만, 
그 물고기가 있는 칸은 지나갈 수 있다.
"""
import collections
N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]
shark = 2
for x in range(N):
    for y in range(N):
        if mat[x][y] == 9:
            sharkPos = (x, y)
            mat[x][y] = 0
            break


def isMap(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


def checkTime(x, y):
    global shark
    global sharkPos
    queue = collections.deque()
    visit = [[0]*N for _ in range(N)]
    queue.append((0, sharkPos[0], sharkPos[1]))
    while queue:
        depth, a, b = queue.popleft()
        visit[a][b] = 1
        if a == x and b == y:
            return depth
        else:
            for dx, dy in [(-1, 0),(0, 1),(0, -1),(1, 0)]:
                nx = a + dx
                ny = b + dy
                if isMap(nx, ny):
                    if mat[nx][ny] <= shark and not visit[nx][ny]:
                        queue.append((depth+1, nx, ny))
    return False

def solve():
    global shark
    global sharkPos
    time = 0
    cnt = 0
    while True:
        prey = {}
        preymat = [[0]*N for _ in range(N)]
        resTime = 0
        for x in range(N):
            for y in range(N):
                if mat[x][y] and mat[x][y] < shark:
                    tempTime = checkTime(x, y)
                    if tempTime:
                        if tempTime not in prey.keys():
                            prey[tempTime] = []
                        prey[tempTime].append((x, y))
        if len(prey) == 0:
            return time
        else:
            thisTime = min(prey.keys())
            thisPrey = sorted(prey[thisTime])[0]
            sharkPos = thisPrey
            cnt += 1
            if shark == cnt:
                cnt = 0
                shark += 1
            time += thisTime
            mat[thisPrey[0]][thisPrey[1]] = 0
print(solve())
