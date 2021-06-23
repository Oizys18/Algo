import sys
sys.stdin = open('BOJ6087.txt','r')
from pprint import pprint as pp


from collections import deque
W,H = map(int,input().split())
mat = [input() for _ in range(H)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

c_pos = []
for x in range(H):
    for y in range(W):
        if mat[x][y] =='C':
            c_pos.append((x,y))


# visit에 방향전환 횟수 체크, bfs 중 visit의 값이 적으면 rewrite 
# visit 1부터 시작, 2가 1회 전환
visit = [[0]*W for _ in range(H)]
def isMap(x,y):
    return 0<=x<H and 0<=y<W and not mat[x][y]=='*'


def solve(x,y):
    mirror = 0
    q = deque()
    q.append((x,y,1,5))
    visit[x][y] = 1 
    while q:
        x,y,turn,dr = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if isMap(nx,ny):
                if i!=dr: 
                    while isMap(nx,ny):
                        if not visit[nx][ny] or visit[nx][ny] > turn+1:
                            q.append((nx,ny,turn+1,i))
                            visit[nx][ny] = turn+1
                        nx,ny = nx+dx[i],ny+dy[i]
                else:
                    while isMap(nx,ny):
                        if not visit[nx][ny] or visit[nx][ny] > turn:
                            q.append((nx,ny,turn,i))
                            visit[nx][ny] = turn
                        nx,ny = nx+dx[i],ny+dy[i]
    return visit[c_pos[1][0]][c_pos[1][1]] - 2

print(solve(c_pos[0][0],c_pos[0][1]))