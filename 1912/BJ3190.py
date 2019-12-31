# 뱀뱀
# rules
"""
길이 1 , 처음에 우측
이동규칙
1. 머리를 다음칸에 위치시킨다.
2. 이동칸에 사과가 있다면, 사과가 없어지고 꼬리는 움직이지 않음
3. 사과가 없다면 몸길이를 줄여서 꼬리칸을 비워준다. 
"""
from pprint import pprint as pp 

N = int(input())
K = int(input())
mat = [[0]*N for _ in range(N)]
apple = []
for k in range(K):
    x, y = map(int, input().split())
    apple.append((x-1, y-1))
mat[0][0] = 1
L = int(input())
rot = {}
for l in range(L):
    X, C = input().split()
    X = int(X)
    rot[X] = C


rotat = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def isMap(x, y):
    if 0 <= x < N and 0 <= y < N:
        if mat[x][y] == 0:
            return True
        else:
            return False
    else:
        return False

def solve(x, y, d, t):
    queue = []
    while True:
        if t in rot.keys():
            if rot[t] == 'D':
                d += 1
                d = d % 4 
            else:
                d -= 1
                if d == -1:
                    d = 3
        nx = x + rotat[d][0]
        ny = y + rotat[d][1]
        
        if isMap(nx, ny):
            t += 1
            queue.append((x, y))
            mat[nx][ny] = 1
            if (nx, ny) not in apple:
                a,b = queue.pop(0)
                mat[a][b] = 0
            else:
                apple.remove((nx,ny))
            x = nx
            y = ny
        else:
            return t+1
        pp(mat)

res = solve(0, 0, 0, 0)
print(res)
