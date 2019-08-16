# SWEA 4861 회문

import sys
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    N,M = map(int,input().split())
    mat = []
    for col in range(N):
        mat.append(input())
    # row 탐색
    result = 0
    for r in range(N):
        for i in range(N-M+1):
            word = mat[r][0+i:M+i]
            if word == word[::-1]:
                result = word 
    # col 탐색  
    if result == 0:
        for c in range(N):
                word = list(zip(*mat))[c][0+i:M+i]
                if word == word[::-1]:
                    result = word
    print("#{0} {1}".format(T+1,result))
