import sys
sys.stdin = open('BOJ15235.txt','r')
from pprint import pprint as pp
"""
During the Olympiad finals we usually serve pizza for the contestants. 
When the food arrives, the contestants to queue to get some pizza. 
Each student will be given a single slice of pizza when his/her turn arrives. 
The problem is that some people need more than one slice of pizza 
to be well fed so they need to queue again for more pizza after they get the first one.

Given a list of slices needed to fed each of the contestants,
 compute how long it will take to fed all of them. We can give a slice of pizza every second 
 and when a contestant is well fed he does not return to the queue.
"""

N = int(input())
slices = [*map(int,input().split())]