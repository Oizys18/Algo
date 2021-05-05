import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1005.txt', 'r')
from heapq import * 
from collections import deque 
def solve(B,total,requirements):
    # total += delays[B-1]
    print('========  B:',B,' total:',total,'  =========')
    # if not ruleD[B]:
    #     return total
    # else:
    #     temp = 0
    #     nxt = 0
    #     for b in ruleD[B]:
    #         if temp <= delays[b-1]:
    #             temp = delays[b-1]
    #             nxt = b 
    #     return solve(nxt,total)
    



    dq = deque(requirements)
    visit = [0]*(N+1)
    visit[B] = 1 
    while dq:
        print(dq)
        build = dq.popleft()
        cost = 0
        nxt_build = 0
        for nxt in ruleD[build]:
            if not visit[nxt]:
                if cost <= delays[nxt-1]:
                    cost = delays[nxt-1]
                    nxt_build = nxt
                    visit[nxt] = 1
        total += cost
        dq.append(nxt_build)
    return total

# 아마도 재귀가 아니라 while문 돌려서 queue로 하나씩 뽑아야할듯?

T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    delays = [*map(int,input().split())]
    rules = [[*map(int,input().split())] for _ in range(K)]
    W = int(input())

    ruleD = {i:[] for i in range(1,N+1)}    
    for rule in rules:
        A,B = rule 
        ruleD[B].append(A)

    print('N,K,W:',N,K,W)
    print('rules:',rules)
    print('ruleDictionary:',ruleD)
    print()
    print('delay:',delays)
    print('                             ')
    print('search answer for ',W,'      ')
    print('answer:',solve(W,0,ruleD[W]))
    print('                             ')
    print('                             ')
    