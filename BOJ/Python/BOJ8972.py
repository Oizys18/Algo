import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ8972.txt', 'r')

R,C = map(int,input().split())
mat = [input() for _ in range(R)]
print(R,C)
pp(mat)