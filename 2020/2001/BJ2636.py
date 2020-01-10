# # 치즈
# import collections
# M, N = map(int, input().split())
# mat = [[*map(int, input().split())] for _ in range(M)]
# visit = [[0]*N for _ in range(M)]


# def isCheese(x, y):
#     if 0 < x < M and 0 < y < N:
#         if mat[x][y] == 1:
#             return True
#         else:
#             return False
#     else:
#         return False


# def solve():
#     time = 0
#     cnt = 0
#     pre = 0
#     while True:
#         visit = [[0]*N for _ in range(M)]
#         for x in range(M):
#             for y in range(N):
#                 if not mat[x][y] and not visit[x][y]:
#                     visit[x][y] = 1
#                     for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
#                         nx = x + dx
#                         ny = y + dy
#                         if isCheese(nx, ny):
#                             mat[nx][ny] = 2
#         flag = 0
#         for x in range(M):
#             for y in range(N):
#                 if mat[x][y] == 2:
#                     flag = 1
#                     cnt += 1
#                     mat[x][y] = 0
#         if cnt == 5:
#             print('22')
#         if not flag:
#             return time, pre
#         pre = cnt
#         cnt = 0
#         time += 1


# print(solve())
