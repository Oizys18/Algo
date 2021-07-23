import sys
sys.stdin = open('BOJ16967.txt','r')
from pprint import pprint as pp

H,W,X,Y = map(int,input().split())
mat = [[*map(int,input().split())] for _ in range(H+X)]
