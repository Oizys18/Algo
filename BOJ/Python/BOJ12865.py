import sys
sys.stdin = open('BOJ12865.txt','r')
from pprint import pprint as pp
N, K = map(int,input().split())
goods = [[*map(int,input().split())] for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

# 배낭문제, dp해야함 
def solve(K,N,goods):
    for i in range(N):
        for w in range(K):
            print(i,w)
            print(goods[i][0])
            if goods[i][0] > K:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(goods[i][1]+ dp[i][K-goods[i][0]],dp[i][w])
    return dp[N][K]
    
print(solve(K,N,goods))
pp(dp)


"""
#Brute force, 어림도 없다.. ㅠ 

N, K = map(int,input().split())
goods = [[*map(int,input().split())] for _ in range(N)]
answer = 0
def backpack(now,total,value):
    global answer 
    if now == N:
        answer = max(value,answer)
        return 
    else:
        if total + goods[now][0] <= K:
            backpack(now+1,total+goods[now][0],value+goods[now][1])
        backpack(now+1,total,value)
        
backpack(0,0,0)
print(answer)
"""