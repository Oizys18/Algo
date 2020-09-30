# 백준 RGB거리

import sys
from pprint import pprint as pp 
sys.stdin = open('1149.txt', 'r')


# 내 풀이 
# N = int(input())
# mat = [[*map(int, input().split())] for _ in range(N)]

# minCost = 1000000
# turnMin = [0]*N

# def solve(pre,cost,k):
#     global minCost 
#     if k == N:
#         if minCost > cost:
#             minCost = cost 
#         return 
#     else:
#         if cost + min(mat[k]) > minCost:
#             return 
#         for color in range(3):
#             if pre == color:
#                 continue
#             if cost+mat[k][color] > minCost:
#                 continue
#             solve(color,cost+mat[k][color], k+1)

# solve(-1,0,0)
# print(minCost)

N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]
DP = [[0]*3 for _ in range(N+1)]
for i in range(3):
    DP[0][i] = mat[0][i] #0번째 줄의 최소 값은 그냥 자기 자신임 

for turn in range(1,N):
    DP[turn][0] = min(DP[turn-1][1],DP[turn-1][2] + mat[turn][0])
    DP[turn][1] = min(DP[turn-1][0],DP[turn-1][2] + mat[turn][1])
    DP[turn][2] = min(DP[turn-1][0],DP[turn-1][1] + mat[turn][2])
    

