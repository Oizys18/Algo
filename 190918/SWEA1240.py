#SWEA1240 단순2진암호

import sys 
sys.stdin = open('input.txt','r')

for T in range(int(input())):
    N, M = map(int,input().split())
    mat = [input().strip('0') for _ in range(N)]
print(mat)