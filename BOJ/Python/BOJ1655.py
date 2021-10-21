from pprint import pprint as pp 

import sys
sys.stdin = open('BOJ1655.txt', 'r')
from heapq import * 
left,right = [],[] 
N = int(input())
for n in [int(sys.stdin.readline()) for _ in range(N)]:
    if len(left) == len(right):
        heappush(left,(-n,n))
    else:
        heappush(right,(n,n))
    if len(left) and len(right) and left[0][1] > right[0][1]:
        maxValue = heappop(left)[1]
        minValue = heappop(right)[1]
        heappush(left,(-minValue,minValue))
        heappush(right,(maxValue,maxValue))
    print(left[0][1])





"""
input() 과 sys.stdin.readline()은 하는 역할과 동작이 다르다. 
https://buyandpray.tistory.com/7
https://jjangsungwon.tistory.com/87 참고 
"""