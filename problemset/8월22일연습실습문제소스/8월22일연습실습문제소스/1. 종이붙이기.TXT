import sys
sys.stdin = open("input.txt", "r")


def fr(n):
    if n == 1 : return 1
    if n == 2 : return 3

    return fr(n - 1) + 2 * fr(n - 2)


def fm(n):
    if DP[ n ]: return DP[n]
    DP[ n ] = fm(n - 1) + 2 * fm(n - 2)
    return DP[n]


def fi():
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 3

    for i in range(2, 101):
        dp[i] = dp[i-1] + 2 * dp[i-2]



DP = [0] * 101
DP[1] = 1
DP[2] = 3

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) // 10
    print('#%d'%tc, fm(N))

