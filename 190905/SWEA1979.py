# SWEA 1979 

import sys
from pprint import pprint
sys.stdin = open('input3.txt','r')
def cnt(line, k):
    stack = []
    temp = list(line)
    res = 0
    while temp:
        a = temp.pop(0)
        if a == 1:
            stack.append(a)
        elif a == 0:
            if len(stack) == k:
                res += 1
                stack = []
            else:
                stack = []
    if len(stack) == k:
        res += 1
    return res



for T in range(int(input())):
    N, K = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    rmat = list(zip(*mat))
    result = 0
    for x in mat:
        result += cnt(x,K)
    for y in rmat:
        result += cnt(y,K)
    print("#{} {}".format(T+1,result))