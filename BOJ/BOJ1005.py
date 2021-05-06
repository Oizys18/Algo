import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1005.txt', 'r')

from collections import deque 
def solve(B,total,requirements):
    dq = deque()
    dq.append(B)
    visit = [0]*(N+1)
    while dq:
        print('dq:',dq)
        build = dq.popleft()
        print('popped node:',build)
        total += delays[build-1]
        print('added total:',total)
        if not visit[build]:
            visit[build] =1
            nxt_build = 0
            cost = 0
            pre_build = set()
            for nxt in ruleD[build]:
                if not visit[nxt]:
                    pre_build.update(ruleD[nxt])
            print('선테크:',pre_build)
            for nxt in ruleD[build]:
                if not visit[nxt] and nxt not in pre_build:
                    if cost <= delays[nxt-1]:
                        cost = delays[nxt-1]
                        nxt_build = nxt
            print('다음빌드:',nxt_build)  
            print('--------------------')       
            if nxt_build:
                dq.append(nxt_build)
    return total

def solve_recur(W,now,total):
    


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
    
    print(solve(W,0,ruleD[W]))