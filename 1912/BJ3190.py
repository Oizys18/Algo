# 뱀뱀
# rules
"""
길이 1 , 처음에 우측
이동규칙
1. 머리를 다음칸에 위치시킨다.
2. 이동칸에 사과가 있다면, 사과가 없어지고 꼬리는 움직이지 않음
3. 사과가 없다면 몸길이를 줄여서 꼬리칸을 비워준다. 
"""

N = int(input())
K = int(input())
mat = [[0]*N for _ in range(N)]
for k in range(K):
    x, y = map(int, input().split())
    mat[x-1][y-1] = 2
mat[0][0] = 1
L = int(input())
rot = {}
for l in range(L):
    X, C = input().split()
    X = int(X)
    rot[X] = C


def solve(x, y):
    queue = []
    queue.append((x, y))
    while queue:
        x, y = queue.pop(0)
        if not visit[x][y]:
            visit[x][y] = 1
            
