#SWEA2817 부분수열의 합
"""
N개의 자연수, 최소 1개 이상의 수를 선택하여 그 합이 K가 되는 경우의 수를 구하기
"""

import sys
sys.stdin = open('input.txt','r')

import itertools
for T in range(int(input())):
    N, K = map(int,input().split())
    numli = list(map(int,input().split()))
    cnt = 0
    for i in range(1,N+1):
        temp = itertools.combinations(numli,i)
        for t in temp:
            if sum(t) == K:
                cnt += 1
    print("#{} {}".format(T+1,cnt))

    
