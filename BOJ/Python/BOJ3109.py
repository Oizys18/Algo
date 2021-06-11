import sys
sys.stdin=open('BOJ3109.txt','r')

from pprint import pprint as pp

R,C = map(int,input().split())
mat =[input() for _ in range(R)]
pipes = [(-1,1),(0,1),(1,1)]


def isEmpty(x,y):
    return 0 <= x < R and 0 <= y < C and mat[x][y]=='.'

def solve(x,y,visited):
    if y == C-1:

        return 'arrived'
    else:
        for i in range(3):
            nx,ny = x+pipes[i][0], y+pipes[i][1]
            if isEmpty(nx,ny) and not visit[nx][ny]:
                visit[nx][ny] = 1 
                visited.add((nx,ny))
                return solve(nx,ny,visited)
                visited.remove((nx,ny))
                visit[nx][ny] = 0
    return visited

visit =[[0]*C for _ in range(R)]
answer = 0
for i in range(R):
    tried = solve(i,0,set())
    if tried=='arrived':
        answer += 1
    else:
        for x,y in tried:
            visit[x][y]=0
    pp(visit)
print(answer)


