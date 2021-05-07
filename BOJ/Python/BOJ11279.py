# 최대 힙 
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ11279.txt', 'r')
from heapq import * 

N = int(input())
data = [int(input()) for _ in range(N)]
hq = []

for d in data:
    if d:
        heappush(hq,(-d,d))
    elif hq and d==0:
        print(heappop(hq)[1])
    else:
        print(0)