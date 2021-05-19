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
    if total_w < L and len(bridge) < w:
        pass
    tiem += 1 
