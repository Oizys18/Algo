#정사각형 방
def isMap(x,y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

        
temp = 0
def DFS(x,y,pre,cnt):
    global temp
    if mat[x][y] - 1 != pre:
        if cnt > temp:
            temp = cnt
        return
    else:
        for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
            nx = x + dx
            ny = y + dy
            if isMap(nx,ny):
                DFS(nx,ny,mat[x][y],cnt+1)
            



T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    mat = [[*map(int,input().split())] for _ in range(N)]
    room = 1001
    res = 0
    for x in range(N):
        for y in range(N):
            temp = 0
            DFS(x,y,mat[x][y]-1,0)
            if temp > res:
                res = temp
                room = mat[x][y]
            elif temp == res and room > mat[x][y]:
                room = mat[x][y]
    print(f"#{testcase} {room} {res}")
 

"""
1
4
13 2 14 12 
10 16 6 5 
1 8 3 15 
7 11 4 9 
"""