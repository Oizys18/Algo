# SWEA 4875 미로
import sys
sys.stdin = open('input3.txt','r')
def bt(start):
    stack = []
    visit = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(pathFinder(node[0],node[1]))
            print(visit)
    return visit

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def pathFinder(x,y):
    path = []
    if (x < N - 1 and x > 0) and (y < N -1 and y > 0):
        while (x < N - 1 and x > 0) and (y < N -1 and y > 0):
            for i in range(4):
                if mat[x+dx[i]][y+dy[i]] in '02' and (x+dx[i],y+dy[i]) not in path:
                    path.append((x+dx[i],y+dy[i]))
            return path
    if x == N - 1 or x == 0:
        while x == N - 1 or x == 0:
            for i in [2,3]:
                if mat[x][y+dy[i]] in '02' and (x,y+dy[i]) not in path:
                    path.append((x,y+dy[i]))
            return path
    if y == 0 or y == N - 1:
        while y == 0 or y == N - 1:
            for i in [0,1]:
                if mat[x+dx[i]][y] in '02' and (x+dx[i],y) not in path:
                    path.append((x+dx[i],y))
            return path



for T in range(int(input())):
    stack = []
    N = int(input())
    
    mat = [input() for _ in range(N)]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '3':
                start = (i,j)
            if mat[i][j] == '2':
                end = (i,j)
    res = bt(start)
    result = 0
    if end in res:
        result = 1

    print("#{0} {1}".format(T+1,result))
    





