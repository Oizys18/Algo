import sys
sys.stdin = open('1949.txt','r')

for T in range(int(input())):
    N, K = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    # valid road?
    def isMap(H, nx, ny): 
        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
            if mat[nx][ny] < H:
                return True
            else:
                return False
        else:
            return False

    # find longest trail possible 
    def BFS(x,y):
        deep = 0
        queue = []
        visit = []
        queue.append((0,x,y))
        while queue:
            depth, a, b = queue.pop(0)
            if depth > deep:
                deep = depth
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if isMap(mat[a][b], nx, ny):
                    queue.append((depth+1,nx,ny))
        return deep + 1
        
    farTrail = 0
    high = 0
    for x2 in range(N):
        for y2 in range(N):
            if mat[x2][y2] >= high:
                high = mat[x2][y2]
    start = []
    for x in range(N):
        for y in range(N):
            if mat[x][y] == high:
                start.append((x,y))
    for i in range(N):
        for j in range(N):
            for x3, y3 in start:
                if i != x3 or j != y3:
                    for k in range(1,K+1):
                        temp = mat[i][j]
                        if mat[i][j] <= k:
                            mat[i][j] = 0
                        else:
                            mat[i][j] -= k
                        trail = BFS(x3, y3)
                        if farTrail < trail:
                            farTrail = trail
                        mat[i][j] = temp
    print(f"#{T+1} {farTrail}")
