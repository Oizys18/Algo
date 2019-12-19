# 테트로미노

# 세로 N 가로 M 
N, M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
def isMap(x,y):
    if 0 <= x < N and 0<= y < M:
        return True
    else:
        return False

tetro = {
    # 길쭉
    0:[(0,1),(0,2),(0,3)],
    1:[(1,0),(2,0),(3,0)],
    # 네모
    2:[(0,1),(1,0),(1,1)],
    # 니은
    3:[(1,0),(2,0),(2,1)],
    4:[(1,0),(2,0),(2,-1)],
    5:[(0,1),(0,2),(1,2)],
    6:[(0,1),(0,2),(-1,2)],
    7:[(1,0),(0,1),(0,2)],
    8:[(-1,0),(0,1),(0,2)],
    9:[(0,-1),(1,0),(2,0)],
    10:[(0,1),(1,0),(2,0)],
    # 뱀
    11:[(1,0),(1,1),(2,1)],
    12:[(1,0),(1,-1),(2,-1)],
    13:[(0,1),(-1,1),(-1,2)],
    14:[(0,1),(1,1),(1,2)],
    # 뻐큐
    15:[(0,1),(0,2),(1,1)],
    16:[(0,1),(0,2),(-1,1)],
    17:[(0,1),(-1,1),(1,1)],
    18:[(1,0),(2,0),(1,1)],
}
temp = 0
tempRes = 0
for x in range(N):
    for y in range(M):
        for t in range(19):
            temp += mat[x][y]
            for a,b in tetro[t]:
                if isMap(x+a,y+b):
                    temp += mat[x+a][y+b]
                else:
                    temp = 0
                    break
            if temp > tempRes:
                tempRes = temp
            temp = 0
print(tempRes)
