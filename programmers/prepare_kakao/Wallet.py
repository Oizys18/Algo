# import sys
# def solution(matrix_sizes):
#     answer = 0
#     temp = matrix_sizes.pop()
#     while matrix_sizes:
#         flag = 0 
#         for i,mat in enumerate(matrix_sizes):
#             if mat[0] == temp[-1]:
#                 flag = 1 
#                 temp.append(mat[1])
#                 break
#             elif mat[1] == temp[0]:
#                 flag = 1 
#                 temp = [mat[0]] + temp 
#                 break
#         if flag:
#             matrix_sizes.pop(i)
#     N = len(temp)
#     dp = [[0]*N for _ in range(N)]
#     for d in range(1, N):
#         for i in range(0,N-d):
#             j = i+d 
#             if d == 1 :
#                 dp[i][j] = temp[i] *temp[j]
#                 continue
#             dp[i][j] = float('inf')
#             for k in range(i+1, j):  # k값으로 최적분할 찾기
#                 dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + temp[i]*temp[k] *temp[j])
#     return dp[1][N-1]

matrix_sizes = [[2,5],[5,10],[10,6]]
# 통과
import sys
def solution(matrix_sizes):
    answer = 0
    matrix = matrix_sizes
    N = len(matrix_sizes)
    dp = [[0]*N for _ in range(N)]
    for diagonal in range(1, N):  # dp[i][i]는 자기 자신의 행렬이기 때문에 값이 0
        for i in range(0, N-diagonal):  # 대각선의 우측 한 칸씩 이동
            j = i + diagonal  # 현재 대각선에서 몇 번째 원소인지
            # 차이가 1밖에 나지 않는 칸
            if diagonal == 1:
                dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
                continue

            dp[i][j] = float('inf')
            # 각 부분행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
            for k in range(i, j):  # k값으로 최적분할 찾기
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
    return dp[0][N-1]

print(solution(matrix_sizes))

dsasd

"""
diagonal: 1 - N 
i: 0 - N-diagonal 
j: 

0 1 4 6
0 0 2 5
0 0 0 3
0 0 0 0 

방문 순서 
0 1 
1 2 
2 3 
0 2 = 0 1 + 1 2 
1 3 = 1 2 + 2 3 
0 3

from pprint import pprint as pp
N = 5
mat = [[0]*N for _ in range(N)]
for d in range(1,N):
    for i in range(0,N-d):
        j = i+d
        mat[i][j] = 1
        for k in range(i+1,j):
            print("d,i,j,k:",d,i,j,k)

        pp(mat)         
"""


