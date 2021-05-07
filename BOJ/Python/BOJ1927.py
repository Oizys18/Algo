import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1927.txt', 'r')

from heapq import *

N = int(input())
hq = []
heapify(hq)
li = [int(input()) for i in range(N)]
for x in li:
    if x:
        heappush(hq,x)
    elif x==0 and hq:
        print(heappop(hq))
    else:
        print(0)


