def solution(money):
    N = len(money)
    # dp : 0번째 집 안훔침 , dp2: 0번째 집 훔침 
    dp = [0]*N
    dp2 = [0]*N
    # 0번째,1번째는 0번째 집을 훔친 값이 최댓값이다. 
    dp2[0] = dp2[1] = money[0]
        
    # 0번째 집을 안훔쳤기 때문에 N-1까지 탐색 
    for j in range(1,N):
        dp[j] = max(dp[j-2]+money[j], dp[j-1])    
    # 0번째 집을 훔쳤기 때문에 N-2까지 탐색 
    for i in range(2,N-1):
        dp2[i] = max(dp2[i-2]+money[i], dp2[i-1])
    return max(dp[N-1],dp2[N-2])

"""
문제 난이도와는 별개로 문제가 굳이 도둑질이어야하는가에 대해선 의문이 있다..
"""