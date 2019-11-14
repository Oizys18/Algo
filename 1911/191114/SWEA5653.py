import sys
sys.stdin = open('5653.txt','r')
from pprint import pprint as pp

testcase = int(input())
tc = 1

def wide(mat):
    # for j in range(n):
    for i in range(len(mat)):
        mat[i] = [0] + mat[i] + [0]
        Mlen = len(mat[i])
    mat.insert(0,[0]*(Mlen))
    mat.append([0]*(Mlen))
        

def virus(K):
    queue = []
    while queue:




for T in range(tc):
    N, M, K = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    


