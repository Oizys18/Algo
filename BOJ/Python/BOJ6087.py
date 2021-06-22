import sys
sys.stdin = open('BOJ6087.txt','r')
from pprint import pprint as pp


from collections import deque
W,H = map(int,input().split())
mat = [input() for _ in range(H)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def solve(x,y):
    mirror = 0
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        