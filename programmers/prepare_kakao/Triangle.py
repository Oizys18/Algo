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

"""
#다른사람 풀이 
내가 똑똑해졌다고 생각하고 깔끔하게 풀었다고 생각했는데, 
그냥 traingle을 업데이트하면서 푼 사람 코드가 있었다. 
풀이법은 똑같았지만 dp를 생성하지 않는 방법을 통해 불필요한 메모리를 사용하지 않은 것 같다 (코드도 간결해진듯 )
"""
def solution(triangle):
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])
