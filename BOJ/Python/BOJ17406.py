from pprint import pprint as pp
# 배열 돌리기 4

import itertools
import copy
N, M, K = map(int, input().split())
mat = [[0]*(M+1)] + [[0]+[*map(int, input().split())] for _ in range(N)]
turnK = [[*map(int, input().split())] for _ in range(K)]

# 시계방향으로 돌리는 함수
# 방향 : 우 하 좌 상 우 하 좌 상 우 하 좌 상
dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dr = 0

def turn(r,c,s):
    global dr
    L = 2*s + 1
    turnMat = [[0]*(M+1)] + [[0]+[0]*M for _ in range(N)]
    for i in range(s+1):
        x, y = r-s+i, c-s+i
        dr = 0
        while True:
            dx,dy = dxdy[dr]
            nx = x + dx
            ny = y + dy
            if r-s <= nx <= r+s and c-s <= ny <= c+s:
                if turnMat[nx][ny] == 0:
                    turnMat[nx][ny] = tempmat[x][y]
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
    turnMat[r][c] = tempmat[r][c]
    for a in range(1,N+1):
        for b in range(1,M+1):
            if turnMat[a][b]:
                tempmat[a][b] = turnMat[a][b]
    
res = []
for tt in itertools.permutations(range(K),K):
    tempmat = copy.deepcopy(mat)  
    for t in tt:
        r,c,s = turnK[t]
        turn(r,c,s)
    for m in tempmat:
        sumM = sum(m)
        if sumM:
            res.append(sumM)
print(min(res))


# for k in turnK:
#     r, c, s = k
#     turn(r,c,s)
# pp(mat)
# res = []
# for m in mat:
#     print(m)
#     res.append(sum(m))
# print(res)


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
