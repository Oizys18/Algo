import sys
sys.stdin = open('input3.txt','r')
def melt():
    mat2 = [[0]* M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if mat[y][x] == 0:
                continue 
            for dx, dy in (-1,0), (1,0), (0,-1),(0, 1):
                newX = x + dx
                newY = y + dy
                if mat[newY][newX] == 0:
                    mat2[y][x] += 1 
    cntIce = 0
    x1 = 0
    y1 = 0
    for y in range(N):
        for x in range(M):
            mat[y][x] -= mat2[y][x]
            if mat[y][x] < 0:
                mat[y][x] = 0
            if mat[y][x]:
                cntIce += 1
                x1 = x
                y1 = y
    return x1, y1, cntIce


def BFS(x, y):
    queue = []
    visit = [[0]* M for _ in range(N)]
    queue.append((x,y))
    visit[y][x] = 1
    cnt = 1

    while queue:
        x, y = queue.pop(0)
        for dx, dy in (-1,0), (1,0), (0,-1),(0, 1):
            newX = x + dx
            newY = y + dy
            if not visit[newY][newX] and mat[newY][newX] > 0:
                queue.append((newX,newY))
                visit[newY][newX] = 1
                cnt += 1
    return cnt


N, M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
    
result = 1
while True:
    # 녹이는 알고리즘 
    x1, y1, cnt = melt()
    #빙산세기 
    if cnt == 0:
        result = 0
        break
    cnt1 = BFS(x1,y1)
    if cnt != cnt1:
        break 
    result += 1
    
print(result)




            
