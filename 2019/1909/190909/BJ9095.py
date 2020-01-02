# DP 
# https://www.acmicpc.net/problem/9095
# BJ9095
# 1 <= n <= 11
"""
n을 1,2,3의 합으로 나타내기 
"""

import sys
sys.stdin = open('input.txt','r')

def calc(N):
    if N == 3:
        return 4
    elif N == 2:
        return 2
    elif N == 1:
        return 1
    else:
        if N % 2 == 0:
            
for T in range(int(input())):
    n = int(input())

