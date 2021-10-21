from pprint import pprint as pp 

import sys
sys.stdin = open('BOJ2696.txt', 'r')
from heapq import * 
T = int(input())
for _ in range(T):
    left,right = [],[] 
    N = int(input())
    K = N//10 +1
    print(N//2+1)
    cnt = 0 
    for _ in range(K):
        nums = [*map(int,sys.stdin.readline().split())]
        for n in range(len(nums)):
            if len(left) == len(right):
                heappush(left,(-nums[n],nums[n]))
            else:
                heappush(right,(nums[n],nums[n]))
            if len(left) and len(right) and left[0][1] > right[0][1]:
                maxValue = heappop(left)[1]
                minValue = heappop(right)[1]
                heappush(left,(-minValue,minValue))
                heappush(right,(maxValue,maxValue))
            if n%2==0:
                print(left[0][1],end=" ")
                cnt += 1
        if N>10:
            if cnt%10 == 0:
                print('')
        else:
            print('')





"""
1655 푸는 김에 풀었다. 
"""