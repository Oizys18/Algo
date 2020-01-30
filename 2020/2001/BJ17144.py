# 바이바이 미세먼지
from pprint import pprint as pp 


R, C, T = map(int, input().split())
mat = [[*map(int, input().split())] for _ in range(R)]
cleaner = []
dust = {}
drx = [0, 0, -1, 1]
dry = [-1, 1, 0, 0]

for x in range(R):
    for y in range(C):
        if mat[x][y]:
            if mat[x][y] == -1:
                cleaner.append((x, y))
            elif mat[x][y]:
                dust[(x, y)] = mat[x][y]



def isMap(x, y):
    if 0 <= x < R and 0 <= y < C:
        return True
    else:
        return False

def addDust():
    global dust
    global mat
    temp = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if mat[x][y] and mat[x][y] != -1:
                cnt = 0
                for i in range(4):
                    nx = x + drx[i]
                    ny = y + dry[i]
                    if isMap(nx, ny):
                        if mat[nx][ny] != -1:
                            temp[nx][ny] += int(mat[x][y] / 5)
                            cnt += 1
                mat[x][y] = mat[x][y] - (int(mat[x][y]/5))*cnt

    for ar in range(R):
        for bc in range(C):
            if temp[ar][bc]:
                mat[ar][bc] += temp[ar][bc]


# 위
upWindDr = [(0, 1), (-1, 0), (0, -1), (1, 0)]
upWindIdx = 0
# 아래
downWindDr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
downWindIdx = 0

def workCleaner():
    global mat
    global upWindIdx
    global downWindIdx
    global cleaner
    upWindIdx = 0
    downWindIdx = 0
    upX, upY = cleaner[0]
    downX, downY = cleaner[1]
    windMat = [[0]*C for _ in range(R)]
    visit = [[0]*C for _ in range(R)]
    windMat[upX][upY] = -1
    windMat[downX][downY] = -1

    # upWind
    kx = upX
    ky = upY

    while upWindIdx < 4:
        ux, uy = upWindDr[upWindIdx]
        nx, ny = kx + ux, ky + uy
        if mat[kx][ky] == -1:
            windMat[nx][ny] = 0
            visit[nx][ny] = 1
            kx = nx
            ky = ny
            continue 

        if isMap(nx, ny):
            if mat[nx][ny] == -1:
                # upWindIdx += 1
                # continue
                break
            
            if mat[kx][ky] != -1:
                windMat[nx][ny] = mat[kx][ky]
            visit[nx][ny] = 1
            kx = nx
            ky = ny
        else:
            upWindIdx += 1
            continue
    
    # downWind
    lx = downX
    ly = downY
    
    while downWindIdx < 4:
        dx, dy = downWindDr[downWindIdx]
        nx, ny = lx + dx, ly + dy
        if mat[lx][ly] == -1:
            windMat[nx][ny] = 0
            visit[nx][ny] = 1
            lx = nx
            ly = ny
            continue 
        
        if isMap(nx, ny):
            if mat[nx][ny] == -1:
                break
            if mat[lx][ly] != -1:
                windMat[nx][ny] = mat[lx][ly]
            visit[nx][ny] = 1
            lx = nx
            ly = ny
        else:
            downWindIdx += 1
            continue

    for a in range(R):
        for b in range(C):
            if visit[a][b]:
                mat[a][b] = windMat[a][b]
    mat[upX][upY] = -1
    mat[downX][downY] = -1

def timeLapse(time):
    global mat
    global cleaner
    while True:
        addDust()
        workCleaner()

        time -= 1
        if time == 0:
            res = 0
            for x in range(R):
                for y in range(C):
                    if mat[x][y] and mat[x][y] != -1:
                        res += mat[x][y]
            return res

print(timeLapse(T))
