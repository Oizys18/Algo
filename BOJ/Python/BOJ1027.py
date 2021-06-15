import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ1027.txt', 'r')

N = int(input())
buildings = [*map(int,input().split())]

print(N)
print(buildings)

def solve(N,buildings):
    for i in range(N):
        top = 0
        for j in range(i+1,N):
            # 가시 확인 
            
            # 탑 재설정 
            top = max(buildings[j],top)
            

solve(N,buildings)