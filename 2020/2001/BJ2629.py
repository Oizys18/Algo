# 양팔저울 
N = int(input())
weight = [*map(int,input().split())]
M = int(input())
marble = [*map(int,input().split())]

양팔저울
N = int(input())
dp = [[0]*15001 for _ in range(31)]
# weight = [0]*31
check = [-1, 0, 1]


weight = [*map(int, input().split())]

M = int(input())
marble = [*map(int, input().split())]

def solve():
    dp[0][0] = 1
    for i in range(N):
        for j in range(3):
            for k in range(15001):
                nextW = weight[i] * check[j] + k
                dp[i][abs(nextW)] = dp[i-1][k]

# solve()


# print(dp[N][4])

# for m in range(M):
#     if dp[N][marble[m]+15000]:
#         print('Y')
#     else:
#         print('N')


# 양팔저울 retry

# N = int(input())
# weights = [*map(int, input().split())]
# M = int(input())
# marbles = [*map(int, input().split())]
# visit = [[0]*15001 for _ in range(31)]


# def solve(n, w):
#     if n > N:
#         return
#     if visit[n][w] == 1:
#         return
#     visit[n][w] = 1
#     for i in range(N):
#         if not visit[n+1][w+weights[i]]:
#             solve(n+1, w+weights[i])
#         if not visit[n+1][w]:
#             solve(n+1, w)
#         if not visit[n+1][abs(w-weights[i])]:
#             solve(n+1, abs(w-weights[i]))
# solve(0, 0)

# for m in marbles:
#     check = 'N'
#     for n in range(N):
#         if visit[n][m]:
#             check = 'Y'
#     print(check)
# print(visit[2][2])