import sys 
sys.stdin = open('BOJ7569.txt','r')
from pprint import pprint as pp 

M,N,H = map(int,input().split())
mat = [[*map(int,input().split())] for _ in range(N)]

pp(mat)