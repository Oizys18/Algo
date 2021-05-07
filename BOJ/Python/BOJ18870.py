import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ18870.txt', 'r')
from heapq import * 

N = int(input())
Xs = [*map(int,input().split())]
hq = []
xd = dict()
for i in range(N):
    if not xd.get(Xs[i]):
        heappush(hq,Xs[i])
        xd[Xs[i]] = []
    xd[Xs[i]].append(i)

cnt = 0
while hq:
    nx = heappop(hq)
    for i in xd[nx]:
        Xs[i] = cnt
    cnt += 1
print(*Xs)