import sys
sys.stdin = open('input3.txt','r')

M, N = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(M)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def isMap(x, y):
    if (x >= 0 and x <= N - 1) and (y >= 0 and y <= M - 1):
        if mat[y][x] == 0:
            return True
        else:
            return False
    else:
        return False
        
def isIceberg(x, y):
    if (x >= 0 and x <= N - 1) and (y >= 0 and y <= M - 1):
        if mat[y][x]:
            return True
        else:
            return False
    else:
        return False

# def BFS(x, y):
#     stack = []
#     stack.append((x,y))
#     while stack:
#         dot = stack.pop(0)
#         if dot not in visit:
#             visit.append(dot)
#             for i in range(4):
#                 newX = x + dx[i]
#                 newY = y + dy[i]
#                 if isIceberg(newX, newY):
#                     stack.append((newX, newY))

# dan = 1
def BFS(x,y,icebergNum,iceVisit):
    visit = iceVisit
    stack = []
    stack.append((icebergNum,x,y))
    while stack:
        dot = stack.pop(0)
        icebergNum, x, y = dot
        if (x,y) not in visit:
            visit.append((x,y))
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                if isIceberg(newX,newY):
                    stack.append((icebergNum,newX,newY))
    return visit



while True:
    cntYear = 0
    icebergNum = 1
    iceVisit = []
    # 빙하갯수 세기 
    for y in range(M):
        for x in range(N):
            if mat[y][x]:
                iceVisit.extend(BFS(x,y,icebergNum,iceVisit))
                icebergNum += 1
                print(iceVisit)

    # 녹이는 알고리즘 
    melt = {}
    for y in range(M):
        for x in range(N):
            zeros = 0
            if mat[y][x]:
                for i in range(4):
                    newX = x + dx[i]
                    newY = y + dy[i]
                    if isMap(newX, newY):
                        zeros += 1
                if mat[y][x] < zeros:
                    zeros = mat[y][x] 
                melt[(x,y)] = zeros  
    for y in range(M):
        for x in range(N):
            if mat[y][x]:
                mat[y][x] -= melt[(x,y)]
    cntYear += 1 


print(cntYear)
    

    
            
