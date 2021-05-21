# Truck 
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ13335.txt', 'r')

# 트럭수, 다리길이, 최대하중 
n,w,L = map(int,input().split())
que = [*map(int,input().split())]
crossed = 0
bridge = []
total_w = 0
time = 0 

while crossed != n:
    
    if bridge:
        for i in range(len(bridge)):
            bridge[i][0] += 1 
        if bridge[0][0] == w+1:
            arrived = bridge.pop(0)
            total_w -= arrived[1]
            crossed += 1 
    if que:
        now = que[0]
        if total_w + now <= L:
            now = que.pop(0)
            total_w += now
            bridge.append([1,now])
    time += 1 
print(time)
    
