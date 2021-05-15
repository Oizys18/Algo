import sys
sys.stdin = open('BOJ2632.txt','r')
from pprint import pprint as pp 
from itertools import cycle 

N = int(input())
m,n = map(int,input().split())
A = cycle([int(input()) for _ in range(m)])
B = cycle([int(input()) for _ in range(n)])

