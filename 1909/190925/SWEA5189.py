#SWEA 5189 전자카트

import sys
sys.stdin = open('input2.txt','r')


import itertools
for T in range(int(input())):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    edges = {}
    result = 100 * N 
    # flag = 0
    for permu in itertools.permutations(range(1,N),N-1):
        li = [0] + list(permu) + [0]
        res = 0
        for i in range(N):
            res += mat[li[i]][li[i+1]]
            if res > result:
                continue
        if res < result:
            result = res
    print("#{} {}".format(T+1,result))

