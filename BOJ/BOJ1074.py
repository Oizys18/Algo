# Z
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1074.txt', 'r')
from collections import deque

N,r,c = map(int,input().split())
visit = [[0]*4 for _ in range(4)]
ans = [[0,1],[2,3]]

def getStart(r,c,mid,start=0):
    counter = mid**2
    rflag = 0
    cflag = 0
    if r >= mid:
        r = r-mid
        rflag=1
    if c >= mid:
        c = c-mid
        cflag=1
    
    if rflag and cflag:
        start += counter*3 
    elif rflag and not cflag:
        start += counter*2 
    elif not rflag and cflag:
        start += counter 
    
    if mid == 1:
        return [r,c,start]
    else:
        return getStart(r,c,mid//2,start)

a,b,c = getStart(r,c,2**(N-1),0)
print(ans[a][b] + c)