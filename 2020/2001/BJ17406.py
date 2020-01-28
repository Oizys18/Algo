from pprint import pprint as pp
# 배열 돌리기 4

N, M, K = map(int, input().split())
mat = [[0]*(M+1)] + [[0]+[*map(int, input().split())] for _ in range(N)]
turnK = [[*map(int, input().split())] for _ in range(K)]
pp(mat)

# 시계방향으로 돌리는 함수
# 방향 : 우 하 좌 상 우 하 좌 상 우 하 좌 상
dxdy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dr = 0

def turn(r,c,s):
    global dr
    L = 2*s + 1
    turnMat = [[0]*(M+1)] + [[0]+[0]*M for _ in range(N)]
    x, y = r-s, c-s
    while True:
        pp(turnMat)
        dx,dy = dxdy[dr]
        nx = x + dx
        ny = y + dy
        if r-s <= nx < r+s+1 and r-s <= ny <= r+s+1:
            print(nx,ny)
            if turnMat[nx][ny] == 0:
                turnMat[nx][ny] = mat[x][y]
                x = nx
                y = ny
            else:
                dr += 1
                if dr > 3:
                    break
                continue
        else:
            dr += 1
            if dr > 3:
                break
            continue
        
    pp(turnMat)



for k in turnK:
    r, c, s = k
    dr = 0
    # print(mat[r-s][c-s])
    turn(r,c,s)



# def turn(r, c, s):
#     global dr
#     def isMap(x, y):
#         if 0 <= x < N and 0 <= y < M:
#             if turnMat[x][y] == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return False

#     def move(x, y):
#         global dr
#         while True:
#             flag = 0
#             dx, dy = dxdy[dr]
#             nx, ny = x + dx, y + dy
#             if isMap(nx, ny):
#                 turnMat[nx][ny] = mat[x][y]
#                 x = nx
#                 y = ny
#             else:
#                 dr += 1
#                 if dr > 3:
#                     dr = 0
#                     break


#     L = 2*s + 1
#     turnMat = [[0]*M for _ in range(N)]
#     for i in range(s+1):
#         print('##')
#         dr = 0
#         move(r-s+i-1, c-s+i-1)
#         pp(turnMat)
#     # pp(turnMat)


# for k in turnK:
#     r, c, s = k
#     turn(r, c, s)
