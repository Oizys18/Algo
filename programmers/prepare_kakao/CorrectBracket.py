def solution(n):
    dp = [0]*(n+1)
    dp[0] = 1 
    dp[1] = 1
    for i in range(2,n+1):
        for j in range(1,i+1):
            dp[i] += dp[i-j] * dp[j-1];     
    return dp[n]    

"""
카탈란 수라고 한다. 
https://bb-dochi.tistory.com/51
https://programmers.co.kr/learn/courses/30/lessons/12929
"""
