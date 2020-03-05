# 아기상어

"""
아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 
나머지 칸은 모두 지나갈 수 있다. 
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
따라서, 크기가 같은 물고기는 먹을 수 없지만, 
그 물고기가 있는 칸은 지나갈 수 있다.
"""
# import collections
# from queue import PriorityQueue
N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]
size = 2
for x in range(N):
    for y in range(N):
        if mat[x][y] == 9:
            shark = (x, y)
            mat[x][y] = 0
            break

def isMap(x, y):
    global size
    if 0 <= x < N and 0 <= y < N:
        if mat[x][y] <= size:
            return True
    else:
        return False

# 도달 가능? 거리는?
def BFS():
    global size
    global shark
    # Pqueue = PriorityQueue()
    Pqueue = []
    # queue = collections.deque()
    queue = []
    visit = [[0]*N for _ in range(N)]
    visit[shark[0]][shark[1]] = 1
    queue.append((0, shark[0], shark[1]))

    while queue:
        # depth, x, y = queue.popleft()
        depth, x, y = queue.pop(0)
        if mat[x][y] and mat[x][y] < size:
            Pqueue.append((depth, x, y))
        if len(Pqueue) > 4:
            return Pqueue
        for dx, dy in [(-1, 0),(0, -1),(0, 1),(1, 0)]:
            nx = x + dx
            ny = y + dy
            if isMap(nx, ny):
                if not visit[nx][ny]:
                    queue.append((depth+1, nx, ny))
                    visit[nx][ny] = 1
    return Pqueue

def solve():
    global size
    global shark
    time = 0
    cnt = 0
    while True:
        pq = BFS()
        # if pq.empty():
        #     return time
        if len(pq)==0:
            return time
        far, a, b = sorted(pq)[0]
        time += far
        shark = (a, b)
        mat[a][b] = 0
        cnt += 1 
        if cnt == size:
            cnt = 0
            size += 1
print(solve())


# 우선순위 큐
# (거리, x, y))
# BFS돌려서 해당 공간에 visit 가능하고 물고기 먹을 수 있으면 pq에 넣음


# import collections
# N = int(input())
# mat = [[*map(int, input().split())] for _ in range(N)]
# shark = 2
# for x in range(N):
#     for y in range(N):
#         if mat[x][y] == 9:
#             sharkPos = (x, y)
#             mat[x][y] = 0
#             break


# def isMap(x, y):
#     if 0 <= x < N and 0 <= y < N:
#         return True
#     else:
#         return False


# def checkTime(x, y):
#     global shark
#     global sharkPos
#     queue = collections.deque()
#     visit = [[0]*N for _ in range(N)]
#     queue.append((0, sharkPos[0], sharkPos[1]))
#     while queue:
#         depth, a, b = queue.popleft()
#         visit[a][b] = 1
#         if a == x and b == y:
#             return depth
#         else:
#             for dx, dy in [(-1, 0),(0, 1),(0, -1),(1, 0)]:
#                 nx = a + dx
#                 ny = b + dy
#                 if isMap(nx, ny):
#                     if mat[nx][ny] <= shark and not visit[nx][ny]:
#                         queue.append((depth+1, nx, ny))
#     return False

# def solve():
#     global shark
#     global sharkPos
#     time = 0
#     cnt = 0
#     while True:
#         prey = {}
#         preymat = [[0]*N for _ in range(N)]
#         resTime = 0
#         for x in range(N):
#             for y in range(N):
#                 if mat[x][y] and mat[x][y] < shark:
#                     tempTime = checkTime(x, y)
#                     if tempTime:
#                         if tempTime not in prey.keys():
#                             prey[tempTime] = []
#                         prey[tempTime].append((x, y))
#         if len(prey) == 0:
#             return time
#         else:
#             thisTime = min(prey.keys())
#             thisPrey = sorted(prey[thisTime])[0]
#             sharkPos = thisPrey
#             cnt += 1
#             if shark == cnt:
#                 cnt = 0
#                 shark += 1
#             time += thisTime
#             mat[thisPrey[0]][thisPrey[1]] = 0
# print(solve())
"""
6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
(3, 1) 2 2 2
(4, 2) 2 3 4
(3, 2) 1 3 5
(1, 2) 2 3 7
(0, 3) 2 4 9
(0, 2) 1 4 10
(1, 1) 2 4 12
(2, 1) 1 4 13
(2, 0) 1 5 14
(1, 0) 1 5 15
(0, 1) 2 5 17
(0, 4) 3 5 20
(0, 5) 1 5 21
(1, 4) 2 6 23
(1, 3) 1 6 24
(2, 3) 1 6 25
(3, 3) 1 6 26
(3, 4) 1 6 27
(3, 5) 1 6 28
(4, 5) 1 7 29
(4, 4) 1 7 30
(4, 3) 1 7 31
(5, 3) 1 7 32
(5, 2) 1 7 33
(5, 1) 1 7 34
(4, 1) 1 7 35
(4, 0) 1 8 36
(3, 0) 1 8 37
(5, 0) 2 8 39
(5, 4) 4 8 43
(5, 5) 1 8 44
(2, 5) 3 8 47
(1, 5) 1 8 48
(2, 4) 2 8 50
(0, 0) 6 9 56
56
"""