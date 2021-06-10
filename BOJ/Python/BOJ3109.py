import sys
sys.stdin=open('BOJ3109.txt','r')

from pprint import pprint as pp


from collections import deque
R,C = map(int,input().split())
mat =[input() for _ in range(R)]
pipes = [(-1,1),(0,1),(1,1)]

pp(mat)

def isEmpty(x,y):
    return 0 <= x < R and 0 <= y < C and mat[x][y]=='.'

def solve(x,y):
    if y == C-1:
        print('도착!')
        pp(visit)
        return 
    else:
        for i in range(3):
            nx,ny = x+pipes[i][0], y+pipes[i][1]
            print(nx,ny)
            if isEmpty(nx,ny) and not visit[nx][ny]:
                visit[nx][ny] = 1 
                return solve(nx,ny)
                visit[nx][ny] = 0

visit =[[0]*C for _ in range(R)]
for i in range(C):
    solve(0,i)
    
"""
직전 탐색 데이터 저장 방법 필요 
"""
