# BJ2636 
import sys
sys.stdin = open('input5.txt','r')
X, Y = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(X)]
# print(mat)
"""
1. 겉부분만 선택하기 
    - 여백에 BFS
    - 동일한 Y*X 행렬2만들어서 
        - 방문한 곳을 2로체크 
        - 껍데기 발견하면 1
            cnt += 1
2. 제거할 부분의 갯수(cnt)와 전체 갯수totalcnt 체크
    - cnt와 totlacnt 비교 
2-1. 다를 경우 칸의 시간+1 하고 제거한 행렬을 업데이트 
2-2. 같을 경우 칸의 시간+1, 칸의 갯수 출력  
"""

def isMap(x,y):
    if (x >= 0 and x <= X-1) and (y >= 0 and y <= Y-1):
        return True
    else:
        return False

def BFS(x, y):
    mat2 = [[0]*Y for _ in range(X)]
    queue = []
    queue.append((x,y))
    cnt = 0
    while queue:
        x,y = queue.pop(0)
        if mat2[x][y] == 0:
            mat2[x][y] = 2
            for dx,dy in (0,1), (0,-1), (-1,0), (1,0):
                newX = x + dx
                newY = y + dy
                if isMap(newX,newY):
                    if mat[newX][newY] == 0:
                        queue.append((newX,newY))
                    elif mat[newX][newY] == 1 and mat2[newX][newY] == 0:
                        mat2[newX][newY] = 2
                        cnt += 1
    return cnt, mat2

time = 0
while True:
    cnt, mat2 = BFS(0,0)
    tcnt = 0
    for x in range(X):
        for y in range(Y):
            if mat[x][y] == 1:
                tcnt += 1
    for x in range(X):
        for y in range(Y):
            mat[x][y] -= mat2[x][y]
            if mat[x][y] < 0 :
                mat[x][y] = 0
    if cnt == tcnt:
        print(time+1)
        print(cnt)
        break
    time += 1

