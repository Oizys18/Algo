# SWEA 4008 계산기
import sys
sys.stdin = open('4008.txt','r')


import itertools
from pprint import pprint as pp
int(input())
for T in range(1):
    N = int(input())
    plus, minus, multi, div = map(int,input().split())
    line = list(map(int,input().split()))
    calc = ['+']*plus +['-']*minus + ['*']*multi + ['/']*div        
    calcDict = dict()

    def Cal(pre, operator, post):
        dic = { 
            "+":(lambda a, b : a + b), 
            "-":(lambda a, b : a - b), 
            "*":(lambda a, b : a * b), 
            "/":(lambda a, b : int(a / b)), 
        }
        return dic[operator](pre,post)

    result = []
    C = len(calc)
    temp = [0]*C
    tempRes = [0]*C
    visited = [0]*C
    def perm(x):
        if x == C:
            result.append(temp.copy())
            
        else:
            for i in range(C):
                if visited[i]:
                    continue
                temp[x] = calc[i]
                visited[i] = 1
                perm(x+1)         
                visited[i] = 0

                
    perm(0)
    # pp(result)

    # minRes = 100000000
    # maxRes = -100000000
    # result = set()
