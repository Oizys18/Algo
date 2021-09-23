def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = [[0]*i for i in range(1,N+1)]
    for i in range(N):
        for j in range(len(triangle[i])):
            if i == 0: dp[i][j] = triangle[i][j]
            else:
                if j == 0 :
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    l = triangle[i][j] + dp[i-1][j-1]
                    r = triangle[i][j] + dp[i-1][j]
                    dp[i][j] = max(dp[i][j],l,r)
    return max(dp[N-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle))