import sys
sys.stdin = open('BOJ16235.txt','r')
from pprint import pprint as pp


N,M,K = map(int,input().split())
Amat = [[*map(int,input().split())] for _ in range(N)]
tree_info = [[*map(int,input().split())] for _ in range(M)]