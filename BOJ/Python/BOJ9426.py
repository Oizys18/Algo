import sys
sys.stdin= open('BOJ9426.txt','r')

from heapq import * 

total = 0
first,second = 0,0
N,K = map(int,sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
# for i in range(N):
#     if not first:
#         first = nums[i]
#     elif not second:
#         second = nums[i]
#     else:
#         now = nums[i]
#         if first <= now <= second or second <= now <= first:
#             med = now 
#         elif now <= first <= second or second <= first <= now:
#             med = first
#         elif now <= second <= first or first <= second <= now:
#             med = second
#         total += med 
#         first = second
#         second = now 
# print(total)

"""
N 길이 배열에서 K길이의 구간을 잘라 중간값을 구하는 것이기 때문에, 
세그먼트 트리를 사용해야한다. 
"""