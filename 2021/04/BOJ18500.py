import sys
sys.stdin = open('BOJ18500.txt','r')
from pprint import pprint as pp


R,C = map(int,input().split())

mat = [input() for _ in range(R)]

pp(mat)