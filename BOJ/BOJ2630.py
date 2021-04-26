# from pprint import pprint as pp
# N = int(input())
# mat = [[*map(int, input().split())] for _ in range(N)]
# visit = [[0]*N for _ in range(N)]
# paint = 1

# def solve(x, y):
#     global paint
#     if not visit[x][y]:
#         idx = 0
#         for i in range(N-y):
#             if not visit[x][y+i]:
#                 if mat[x][y+i]:
#                     idx = i
#                 else:
#                     break
#         for a in range(idx+1):
#             for b in range(idx+1):
#                 visit[x+a][y+b] = paint
#         paint += 1

# for x in range(N):
#     for y in range(N):
#         if mat[x][y] == 1:
#             solve(x, y)




# cnt = [0] * (((N//2)**2)*2)
# edge = {}
# for x in range(N):
#     for y in range(N):
#         if visit[x][y]:
#             cnt[visit[x][y]] += 1
# for a in range(N//2):
#     edge[(N//2)**a] = 0

# print(cnt)
# for i in cnt:
#     if i:
#         edge[i] += 1
    
