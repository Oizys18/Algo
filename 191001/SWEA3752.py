import sys
sys.stdin = open('input4.txt','r')
import itertools
# def perm(k):
#     if k == N:
#         print(scores)
#     else:
#         for i in range(k, N):
#             scores[k], scores[i] = scores[i], scores[k]
#             perm(k + 1)
#             scores[k], scores[i] = scores[i], scores[k]

def H_r(k, s):
    if k == R: 
        if not res[sum(t)]:
            res[sum(t)] = 1
            print(sum(t))
        # print(t)
    else:
        for i in range(s, N):
            t[k] = a[i]
            if res[sum(t)] and k == R:
                continue
            # else:
            #     continue
            H_r(k + 1, i)





# def comb_r(k, s):
#     global flag
#     if k == R: 
#         if not res[sum(t)]:
#             res[sum(t)] = 1
#             print(t)
#     else:
#         for i in range(s, N + (k - R) + 1):
#             if flag == 1:
#                 continue
#             if t[k] == a[i]:
#                 flag = 1
#             t[k] = a[i]
#             comb_r(k + 1, i + 1)



for T in range(int(input())):
    N = int(input())
    a = [*map(int,input().split())]
    temp = 0
    res = [0]*(10000)
    # for k in range(N + 1):
    R = N
    t = [0] * R
    H_r(0, 0)

    print("#{} {}".format(T+1,sum(res)))



"""
#1 4680
#2 4566
#3 5646
#4 4891
#5 4357
#6 4773
#7 5482
#8 4971
#9 5158
#10 4847
"""
