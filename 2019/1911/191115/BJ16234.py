from pprint import pprint as pp

N, L, R = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def isMap(x,y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

cnt = 0
def move(mat):
    global cnt
    while True:
        move_li = set()
        for x in range(N):
            for y in range(N):
                pop = mat[x][y]
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if isMap(nx,ny):
                        if (nx,ny) in move_li:
                            continue
                        newPop = mat[nx][ny]
                        if L <= abs(pop-newPop) <= R:
                            move_li.add((nx,ny))
                            move_li.add((x,y))
        pp(mat)
        if len(move_li) == 0:
            return cnt

        total_pop = 0
        for x, y in move_li:
            total_pop += mat[x][y]
        for x, y in move_li:
            mat[x][y] = total_pop // len(move_li) 
        cnt += 1
    
print(move(mat))