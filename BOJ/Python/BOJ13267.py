# Dangerous Dive 
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ13267.txt', 'r')
# N = 총 봉사자 수 R = returned 수 
N,R = map(int,input().split())
volunteers = [0]*(N)
returned = [*map(int,input().split())]
for r in returned:
    volunteers[r-1] = 1 
if sum(volunteers) == N:
    print('*')
else:
    for i in range(N):
        if not volunteers[i]:
            print(i+1,end=' ')