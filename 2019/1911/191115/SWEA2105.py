import sys
from pprint import pprint as pp
sys.stdin = open('2105.txt','r')

def isMap(x, y):
    pass

def eat(x, y):
    
    pass
    


int(input())
for T in range(2):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    pp(mat)

    for x in range(N-2):
        for y in range(1,N-1):
            # 마름모 탐색 시작점 (x,y) 가로 y 세로 x 
            print(mat[x][y])
            print((N-1-y)*(N-1-N+1+y))
            print()
        