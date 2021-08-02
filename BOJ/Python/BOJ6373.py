# https://www.acmicpc.net/problem/6373
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ6373.txt', 'r')
# from itertools import cycle 

while True:
    try:
        N = input()
        lN = len(N)
        start= N[0]
        for j in range(2,lN+1):
            flag = 0
            M = str(j*int(N))
            if len(M) != lN:
                flag = 1 
                break
            for i in range(lN):
                if M[i] == start:
                    print(M)
                    for k in range(lN):
                        if M[(i+k)%lN] != N[k]:
                            flag = 1
                            break 
                    if flag:
                        break
                    print('cycle!')
            if flag:
                break
        if flag:
            print(f"{N} is not cyclic")
        else:
            print(f"{N} is cyclic")
    except:
        break
