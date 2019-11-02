import sys
sys.stdin = open('input.txt','r')
import itertools



for T in range(int(input())):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    res = 100000
    temp = 0
    for i in itertools.permutations(range(N),N):
        for k in range(N):
            temp += mat[k][i[k]]
            if temp > res:
                flag = 1
                break
        # if flag == 1:
        #     temp = 0
        #     flag = 0
        #     break
        if temp < res:
            res = temp
        temp = 0
    print("#{} {}".format(T+1,res))


perm = [i for i in range(N)]

def solve(k, s):
    global ans
    # 그리디
    if k == N:
        ans = min(ans, s)
    else:
        for i in range(k, N):
            perm[i], perm[k] = perm[k], perm[i]
            if s + arr[k][perm[k]] < ans:
                solve(k+1, s + arr[k][perm[k]])
            perm[k], perm[i] = perm[i], perm[k]
