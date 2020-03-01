from pprint import pprint as pp
# 새로운 게임 
# N, K = map(int, input().split())
# mat = [[0]*(N+1)] + [[0]+[*map(int, input().split())] for _ in range(N)]
# pawn_info = [[*map(int, input().split())] for _ in range(K)]
# ride = [[[]]*(N+1) for _ in range(N+1)]
# move = [(0, 1), (0, -1), (-1, 0), (1, 0)]


# def isMap(x, y):
#     if 0 < x < N and 0 < y < N:
#         return True
#     else:
#         return False


# def move_pawn(i):
#     x, y, dr = pawn_info[i-1]
#     # print(x,y,dr)
#     if len(ride[x][y]) > 2:
#         if len(ride[x][y]) == 4:
#             return True
#         if len(ride[x][y][0] != i):
#             return
#         else:
#             nx, ny = x + move[dr][0], y + move[dr][1]
#             if isMap(nx, ny):
#                 # white
#                 if mat[nx][ny] == 0:
#                     if ride[nx][ny]:
#                         ride[nx][ny].append(ride[x][y])
#                         ride[x][y] = []
#                         if len(ride[nx][ny]) == 4:
#                             return True
#                     else:
#                         ride[nx][ny] = ride[x][y]
#                         ride[x][y] = []
#                     pawn_info[i-1][0] = nx
#                     pawn_info[i-1][1] = ny
#                 # red
#                 elif mat[nx][ny] == 1:
#                     if ride[nx][ny]:
#                         ride[nx][ny].append(ride[x][y][::-1])
#                         ride[x][y] = []
#                         if len(ride[nx][ny]) == 4:
#                             return True
#                     else:
#                         ride[nx][ny] = ride[x][y][::-1]
#                         ride[x][y] = []
#                     pawn_info[i-1][0] = nx
#                     pawn_info[i-1][1] = ny

#                 # blue
#                 elif mat[nx][ny] == 2:
#                     if dr == 0:
#                         ndr = 1
#                     elif dr == 1:
#                         ndr = 0
#                     elif dr == 2:
#                         ndr = 3
#                     elif dr == 3:
#                         ndr = 2

#                     nnx, nny = nx + move[ndr][0], ny + move[ndr][1]
#                     # 방향 바꾸고 가려는 블록
#                     if isMap(nnx,nny):
#                         if mat[nnx][nny] == 0:
#                             pawn_info[i-1][2] = ndr
#                             if ride[nnx][nny]:
#                                 ride[nnx][nny].append(ride[x][y])
#                                 if len(ride[nnx][nny]) == 4:
#                                     return True 
#                                 ride[x][y] = []
#                             else:
#                                 ride[nnx][nny] = ride[x][y]
#                                 ride[x][y] = []
#                             pawn_info[i-1][0] = nx
#                             pawn_info[i-1][1] = ny

#                         # red
#                         elif mat[nnx][nny] == 1:
#                             pawn_info[i-1][2] = ndr
#                             if ride[nnx][nny]:
#                                 ride[nnx][nny].append(ride[nx][ny][::-1])
#                                 if len(ride[nnx][nny]) == 4:
#                                     return True
#                                 ride[nx][ny] = []
#                             else:
#                                 ride[nnx][nny] = ride[nx][ny][::-1]
#                                 ride[nx][ny] = []
#                             pawn_info[i-1][0] = nx
#                             pawn_info[i-1][1] = ny

#                         # blue
#                         elif mat[nnx][nny] == 2:
#                             pawn_info[i-1][2] = ndr
#                     else:
#                         pawn_info[i-1][2] = ndr

#             else:
#                 if dr == 0:
#                     ndr = 1
#                 elif dr == 1:
#                     ndr = 0
#                 elif dr == 2:
#                     ndr = 3
#                 elif dr == 3:
#                     ndr = 2

#                 nnx, nny = nx + move[ndr][0], ny + move[ndr][1]
#                 # 방향 바꾸고 가려는 블록
#                 if isMap(nnx,nny):
#                     if mat[nnx][nny] == 0:
#                         pawn_info[i-1][2] = ndr
#                         if ride[nnx][nny]:
#                             ride[nnx][nny].append(ride[x][y])
#                             if len(ride[nnx][nny]) == 4:
#                                     return True
#                             ride[x][y] = []
#                         else:
#                             ride[nnx][nny] = ride[x][y]
#                             ride[x][y] = []
#                         pawn_info[i-1][0] = nx
#                         pawn_info[i-1][1] = ny

#                     # red
#                     elif mat[nnx][nny] == 1:
#                         pawn_info[i-1][2] = ndr
#                         if ride[nnx][nny]:
#                             ride[nnx][nny].append(ride[nx][ny][::-1])
#                             if len(ride[nnx][nny]) == 4:
#                                     return True
#                             ride[nx][ny] = []
#                         else:
#                             ride[nnx][nny] = ride[nx][ny][::-1]
#                             ride[nx][ny] = []
#                         pawn_info[i-1][0] = nx
#                         pawn_info[i-1][1] = ny

#                     # blue
#                     elif mat[nnx][nny] == 2:
#                         pawn_info[i-1][2] = ndr
#                 else:
#                     pawn_info[i-1][2] = ndr

#     else:
#         nx, ny = x + move[dr][0], y + move[dr][1]
#         if isMap(nx, ny):
#             # white
#             if mat[nx][ny] == 0:
#                 if ride[nx][ny]:
#                     ride[nx][ny].append(ride[x][y])
#                     ride[x][y] = []
#                     if len(ride[nx][ny]) == 4:
#                         return True
#                 else:
#                     ride[nx][ny] = ride[x][y]
#                     ride[x][y] = []
#                 pawn_info[i-1][0] = nx
#                 pawn_info[i-1][1] = ny
#             # red
#             elif mat[nx][ny] == 1:
#                 if ride[nx][ny]:
#                     ride[nx][ny].append(ride[x][y][::-1])
#                     ride[x][y] = []
#                     if len(ride[nx][ny]) == 4:
#                         return True
#                 else:
#                     ride[nx][ny] = ride[x][y][::-1]
#                     ride[x][y] = []
#                 pawn_info[i-1][0] = nx
#                 pawn_info[i-1][1] = ny

#             # blue
#             elif mat[nx][ny] == 2:
#                 if dr == 0:
#                     ndr = 1
#                 elif dr == 1:
#                     ndr = 0
#                 elif dr == 2:
#                     ndr = 3
#                 elif dr == 3:
#                     ndr = 2

#                 nnx, nny = nx + move[ndr][0], ny + move[ndr][1]
#                 # 방향 바꾸고 가려는 블록
#                 if isMap(nnx,nny):
#                     if mat[nnx][nny] == 0:
#                         pawn_info[i-1][2] = ndr
#                         if ride[nnx][nny]:
#                             ride[nnx][nny].append(ride[x][y])
#                             if len(ride[nnx][nny]) == 4:
#                                 return True 
#                             ride[x][y] = []
#                         else:
#                             ride[nnx][nny] = ride[x][y]
#                             ride[x][y] = []
#                         pawn_info[i-1][0] = nx
#                         pawn_info[i-1][1] = ny

#                     # red
#                     elif mat[nnx][nny] == 1:
#                         pawn_info[i-1][2] = ndr
#                         if ride[nnx][nny]:
#                             ride[nnx][nny].append(ride[nx][ny][::-1])
#                             if len(ride[nnx][nny]) == 4:
#                                 return True
#                             ride[nx][ny] = []
#                         else:
#                             ride[nnx][nny] = ride[nx][ny][::-1]
#                             ride[nx][ny] = []
#                         pawn_info[i-1][0] = nx
#                         pawn_info[i-1][1] = ny

#                     # blue
#                     elif mat[nnx][nny] == 2:
#                         pawn_info[i-1][2] = ndr
#                 else:
#                     pawn_info[i-1][2] = ndr
#         else:
#             if dr == 0:
#                 ndr = 1
#             elif dr == 1:
#                 ndr = 0
#             elif dr == 2:
#                 ndr = 3
#             elif dr == 3:
#                 ndr = 2

#             nnx, nny = nx + move[ndr][0], ny + move[ndr][1]
#             # 방향 바꾸고 가려는 블록
#             if isMap(nnx,nny):
#                 if mat[nnx][nny] == 0:
#                     pawn_info[i-1][2] = ndr
#                     if ride[nnx][nny]:
#                         ride[nnx][nny].append(ride[x][y])
#                         if len(ride[nnx][nny]) == 4:
#                                 return True
#                         ride[x][y] = []
#                     else:
#                         ride[nnx][nny] = ride[x][y]
#                         ride[x][y] = []
#                     pawn_info[i-1][0] = nx
#                     pawn_info[i-1][1] = ny

#                 # red
#                 elif mat[nnx][nny] == 1:
#                     pawn_info[i-1][2] = ndr
#                     if ride[nnx][nny]:
#                         ride[nnx][nny].append(ride[nx][ny][::-1])
#                         if len(ride[nnx][nny]) == 4:
#                                 return True
#                         ride[nx][ny] = []
#                     else:
#                         ride[nnx][nny] = ride[nx][ny][::-1]
#                         ride[nx][ny] = []
#                     pawn_info[i-1][0] = nx
#                     pawn_info[i-1][1] = ny

#                 # blue
#                 elif mat[nnx][nny] == 2:
#                     pawn_info[i-1][2] = ndr
#             else:
#                 pawn_info[i-1][2] = ndr

# turn = 0
# print('--------')
# flag = 0
# while True:
#     for i in range(1, K+1):
#         if move_pawn(i):
#             flag = 1
#             break
#     turn += 1
#     print(turn)
#     pp(ride)
#     if flag:
#         print(1)
#         break
#     if turn > 5:
#         print(-1)
#         break

#             # print(turn)


#  새롭게 풀어야겠다.. 
#  함수화 시키자.. 
#  복붙은 최소화하자.. 