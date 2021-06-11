import sys
sys.stdin=open('BOJ3109.txt','r')

from pprint import pprint as pp

R,C = map(int,input().split())
mat =[input() for _ in range(R)]
pipes = [(-1,1),(0,1),(1,1)]


def isEmpty(x,y):
    return 0 <= x < R and 0 <= y < C and mat[x][y]=='.'

def solve(x,y):
    if y == C-1:
        return True
    else:
        for i in range(3):
            nx,ny = x+pipes[i][0], y+pipes[i][1]
            if isEmpty(nx,ny) and not visit[nx][ny]:
                visit[nx][ny] = 1 
                if solve(nx,ny):
                    return True
                
    return False

visit =[[0]*C for _ in range(R)]
answer = 0
for i in range(R):
    if solve(i,0):
        answer += 1
print(answer)


