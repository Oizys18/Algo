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



"""
word == word[::-1]을 하는 것보다, 

word를 반으로 나눠서 (len(word)/2)
0부터 len(word)/2 까지 반복하며 
맨 앞과 맨 뒤 비교, 
앞에서 두번째와 뒤에서 두번째 비교, 
요런식으로 반복하는 것이 더 메모리 적게 먹는다. 
"""
