import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ9874.txt', 'r')

N = int(input())
d = dict()
for _ in range(N):
    a,b = map(int,input().split())
    if not d.get(b):
        d[b] = []
    d[b].append(a)
pp(d)    

