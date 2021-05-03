import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ7662.txt', 'r')



from heapq import *

for _ in range(int(input())):
    HQ = []
    for k in range(int(input())):
        w,v = input().split()
        v = int(v)
        if w == 'I':
            heappush(HQ, v)
        elif w == 'D' and HQ:
            if v==1:
                HQ.pop(HQ.index(max(HQ)))
            else:
                heappop(HQ)
    if HQ:
        print(f"{max(HQ)} {min(HQ)}")
    else:
        print('EMPTY')





"""
시간초과
heap은 logN 시간 복잡도 
문제는 최대값을 빼는  
if v==1:
    HQ.pop(HQ.index(max(HQ)))
부분에서 list.index()를 해버리는 것 
-> O(N)

다른 방식을 찾아야한다. 
"""