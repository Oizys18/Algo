# 소가 길을 건너간 이유 6

import sys 
sys.stdin = open('BOJ14466.txt','r')

N, K, R = map(int,input().split())
mat = [[0]*N for _ in range(N)]
road = [list(map(int,input().split())) for _ in range(R)]
cow = {i:tuple(map(int,input().split())) for i in range(K)}

print(N,K,R)
print(road)
print(cow)