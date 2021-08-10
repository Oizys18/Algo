import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ5827.txt', 'r')


N,M = map(int,input().split())
mat = [[*map(int,input().split())] for _ in range(N)]
pp(N,M)
