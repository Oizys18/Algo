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
            if len(M) < lN:
                M = '0'+M
            cycle = 0
            for i in range(lN):
                check = 0
                if M[i] == start:
                    for k in range(lN):
                        if M[(i+k)%lN] == N[k]:
                            check += 1
                    if check == lN:
                        cycle = 1
                        break
            if not cycle:
                flag = 1 
                break
        if flag:
            print(f"{N} is not cyclic")
        else:
            print(f"{N} is cyclic")
    except:
        break
