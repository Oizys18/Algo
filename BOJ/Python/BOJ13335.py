# Truck 
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ13335.txt', 'r')


n,w,L = map(int,input().split())
que = [*map(int,input().split())]

bridge = []
total_w = 0
time = 0 

while que:
    for b in bridge:
        b += 1 
    
    if total_w < L and len(bridge) < w:
        nxt = que.pop(0)
        total_w += nxt 

    time += 1 
