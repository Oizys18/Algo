from pprint import pprint as pp
def isMap(x,y):
    if 0 <= x < N and 0 <= y < M:
        if mat[x][y] == 0:
            return True
        else:
            return False
    else:
        return False


result = 0
def comb(k, s):
    global result
    def BFS(x, y):
        queue = []
        queue.append((x,y))
        tempM[x][y] = 0
        while queue:
            x, y = queue.pop(0)
            if tempM[x][y] == 0:
                tempM[x][y] = 2
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if isMap(nx,ny):
                        queue.append((nx,ny))
    if k == 3:
        tempM = [[0]*M for _ in range(N)]
        for x,y in dic[1]:
            tempM[x][y] = 1
        for wx,wy in temp:
            tempM[wx][wy] = 1
        for a,b in dic[2]:
            BFS(a,b)
        res = 0
        for a in range(N):
            for b in range(M):
                if not tempM[a][b]:
                    res += 1
        if res > result:
            result = res
    else:
        for i in range(s, wall-3+k+1):
            temp[k] = dic[0][i]
            comb(k+1,i+1)

N, M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
dic = {0:[],1:[],2:[],}
for x in range(N):
    for y in range(M):
        if mat[x][y] == 2:
            dic[2].append((x,y))
        elif mat[x][y] == 0:
            dic[0].append((x,y))
        elif mat[x][y] == 1:
            dic[1].append((x,y))

wall = len(dic[0])
dx = [0,0,-1,1]
dy = [-1,1,0,0]
temp = [0]*3
comb(0,0)


print(result)

