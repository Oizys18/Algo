# 색종이 만들기 
import sys
from pprint import pprint as pp 
sys.stdin = open('BOJ2630.txt', 'r')

N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]
dx = [0,0,1,1]
dy = [0,1,0,1]
cntDict = {0:0,1:0}

def solve(sx,sy,M):
    mid = M//2
    ones = 0
    zeros = 0
    if M > 2:
        for x in range(M):
            for y in range(M):
                if mat[x+sx][y+sy]:
                    ones += 1
                else:
                    zeros += 1
        if zeros and ones:
            for i in range(4):
                nx,ny = sx+dx[i]*mid, sy+dy[i]*mid
                solve(nx,ny,mid)
        else:
            if zeros: cntDict[0] += 1 
            if ones: cntDict[1] += 1
    else:
        oneCnt = 0
        zeroCnt = 0
        for x in range(2):
            for y in range(2):
                if mat[sx+x][sy+y]:
                    oneCnt += 1
                else:
                    zeroCnt += 1

        if oneCnt == 4:
            cntDict[1] += 1
        elif zeroCnt == 4:
            cntDict[0] += 1
        else:
            cntDict[1] += oneCnt
            cntDict[0] += zeroCnt

solve(0,0,N)

print(cntDict[0])
print(cntDict[1])


"""

1년전 코드 
BFS 돌면서 paint를 하나씩 증가 시키는 방식인듯 


from collections import deque

N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]
visit = [[0]*N for _ in range(N)]
paint = 1

def solve(x, y):
    global paint
    if not visit[x][y]:
        idx = 0
        for i in range(N-y):
            if not visit[x][y+i]:
                if mat[x][y+i]:
                    idx = i
                else:
                    break
        for a in range(idx+1):
            for b in range(idx+1):
                visit[x+a][y+b] = paint
        paint += 1

for x in range(N):
    for y in range(N):
        if mat[x][y] == 1:
            solve(x, y)




cnt = [0] * (((N//2)**2)*2)
edge = {}
for x in range(N):
    for y in range(N):
        if visit[x][y]:
            cnt[visit[x][y]] += 1
for a in range(N//2):
    edge[(N//2)**a] = 0

print(cnt)
for i in cnt:
    if i:
        edge[i] += 1
    
"""