# BAEKJOON 2667 
"""
DFS를 통해 섬을 찾는다. 
좌표값을 주고받은 후 새로운 mat을 그린다 
"""

dx = [-1,1,0,0]
dy = [0,0,1,-1]
dan = 2

def DFS(x,y):
    global dan
    stack = []
    stack.append((x,y))
    while stack:
        dot = stack.pop()
        x,y = dot
        if mat[y][x] == 1:
            mat[y][x] = dan
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                if isApt(newX,newY):
                    stack.append((newX,newY))
    dan += 1

def isApt(x,y):
    if (x <= N-1 and x >= 0) and (y <= N - 1 and y >= 0):
        if mat[y][x] == 1:
            return True
        else: 
            return False
    else:
        return False

N = int(input())
mat = []
for _ in range(N):
    line = input()
    mat.append([int(x) for x in line])


for y in range(len(mat)):
    for x in range(len(mat[y])):
        if mat[y][x] == 1:
            DFS(x,y)
cnt = {}
for y in range(len(mat)):
    for x in range(len(mat[y])):
        if mat[y][x]:
            if mat[y][x] not in cnt.keys():
                cnt[mat[y][x]] = 1
            else:
                cnt[mat[y][x]] += 1
print(len(cnt.keys()))
nums = sorted([x for x in cnt.values()])
for n in nums:
    print(n)
