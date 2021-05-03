import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1931.txt', 'r')
from heapq import * 

N = int(input())
times = [tuple(map(int,input().split())) for _ in range(N)]
hq = []
for time in times:
    heappush(hq,(time[1],time[0]))
cnt = 1 
e,s = heappop(hq)


for _ in range(N-1):
    time = heappop(hq)
    if e <= time[1]:
        e = time[0]
        cnt += 1 
print(cnt)


"""
고민해보면, 
종료시간이 빠를수록 다른 회의가 더 빨리 시작할 수 있다. 
-> 종료시간이 빠른 회의를 선택하는게 유리하다. 

-> heapq 를 생성, 종료시간을 기준으로 heap 시킴 
-> heappop 하나씩 하면서, 
시작시간이 현재까지 정해진 스케쥴의 종료시간보다 같거나 크면 추가한다. 

"""