import sys
sys.stdin= open('BOJ11657.txt','r')
# 타임머신

N,M = map(int,sys.stdin.readline().split())
mat = [[*map(int,sys.stdin.readline().split())] for _ in range(M)]
print(N,M)
print(mat)