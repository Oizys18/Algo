# SWEA 5188 최소합
import sys
sys.stdin = open('input.txt','r')

dx = [0,1]
dy = [1,0]

def isPath(x,y):
    if (0 <= x <= N-1) and (0 <= y <= N-1):
        return True
    else: 
        return False

def DFS(node):
    global res
    global result 
    x,y = node
    nx,ny = 0,0
    if (x,y) == end and res < result:
        result = res
        return
    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if isPath(nx,ny):
                visit.append((nx,ny))
                res += mat[nx][ny]
                if res > result:
                    res -= mat[nx][ny]
                    visit.pop()
                    continue
                DFS((nx,ny))
                res -= mat[nx][ny]
                visit.pop()
                
for T in range(int(input())):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    res = mat[0][0]
    result = 10000
    visit = [(0,0)]
    end = (N-1,N-1)
    DFS((0,0))
    print("#{} {}".format(T+1, result))