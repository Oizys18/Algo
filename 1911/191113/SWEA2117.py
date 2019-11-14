import sys
from pprint import pprint as pp
sys.stdin = open('2117.txt','r')

for T in range(int(input())):
    N, M = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    def BFS(K,x,y,i,j):
        if abs(x-i) + abs(y-j) < K:
            return 1
        else:
            return 0
    plans = []
    for x in range(N):
        for y in range(N):
            for k in range(1,2*N+1):
                house = 0
                for i in range(N):
                    for j in range(N):
                        if mat[i][j] == 1:
                            house += BFS(k,x,y,i,j)
                if house * M >= (k * k + (k - 1) * (k - 1)):    
                    plans.append(house)
    print(f"#{T+1} {max(plans)}")
    