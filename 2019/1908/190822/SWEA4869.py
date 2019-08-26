#SWEA 4869

import sys
sys.stdin = open('input.txt','r')

def box(n):
    if n == 1:
        return 1
    elif n == 2:
        return box(1) + 2*box(1)
    elif n > 2:
        return box(n-1) + 2 * box(n-2)


"""
# DP로 짜보기.. 데이터 저장으로
# def DP(n):
#     DP = []
#     if DP[n]:
#         return DP[n]
#     if n == 1:
#         return DP[]= 1

#     elif n == 2:
#         return box(1) + 2*box(1)
#     elif n > 2:
#         return box(n-1) + 2 * box(n-2)
"""


for T in range(int(input())):
    N = int(int(input())/10)
    print("#{0} {1}".format(T+1,box(N)))